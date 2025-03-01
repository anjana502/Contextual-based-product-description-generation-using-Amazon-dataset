import warnings

from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch
import time
import math
from nltk.translate.bleu_score import sentence_bleu

# Prepare data
all_headlines=['when my daughter and granddaughter come over, they take what I have sitting out. That means my supply of scrunchies diminish and have to be replenished. These may not be able to make two twists for thick hair, but for thin, it will. Maybe even three.'
 'I just put this on and it was creamy and a small amount can go a long way. I even put some on the outer eye wrinkles and the labial lines. I can feel the tightening as I type.'
 'they are not fragrance free though. As know, essential oils have fragrances to them and you can smell the oils in these two bottles. What is bad, is that they both leaked, even though they had plastic covering the tops and on the upper parts of the bottle. They were shipped in a shipper bag with the poly bubble interior and that was not enough protection.'
 'This will help your skin heal quicker and better than just using regular facial products. OxygenCeuticals makes a fine product that is designed to moisturize, calm and repair skin. You will love it after you start using it.'
 'This helps so much. I have eczema, psoriasis and who knows whatever else and I am always having to treat somewhere. This will help with the cracked skin.'
 "You don't have to use conditioners afterwards. And your scalp feels better. If you have dandruff or eczema, this will most likely help both of those issues. The smell is sweet but tolerable and doesn't last all day. This one you use after you have shampooed your hair and you leave it in 5 minutes. My hair still had tangles though."
 'This kit comes with about everything that is needed. It is packed with 1 tattoo machine pen,1 tattoo power supply,1 tattoo foot pedal, 7pcs tattoo ink, 40pcs tattoo cartridges needles, 1 tattoo grip tape,100pcs tattoo ink cap cups, 1  tattoo transfer paper and 1pcs tattoo kit case. Everything comes packed in the case.'
 'I have decided silk is a wonderful thing. It keeps your hair nice as you sleep and it makes a great, gentle exfoliator that I can use without scratching up my dry legs and arms. I would recommend everyone try this.'
 "and a nose that doesn't get over fragranced easily, this is your cream. It is thick, applies easily and gets absorbed quickly. The scent does dissipates in a fairly good time.<br /><br />Ingredients: Aqua/Water/Eau**, Aqua/Water/Eau, Glycerin, Glyceryl Stearate, Dodecane, Butyrospermum Parkii (Shea) Butter*, Propanediol, Butylene Glycol, Coco-Caprylate/Caprate, Candelilla/Jojoba/Rice Bran Polyglyceryl-3 Esters, Magnesium Aluminum Silicate, Olus Oil/Vegetable Oil/Huile Végétale, Silica, Mel Extract/Honey Extract/Extrait de miel*, Royal Jelly, Cera Alba/Beeswax/Cire d'abeille*, Propolis Extract, Rosa Canina Fruit* Extract, Zizyphus Jujuba Seed Extract, Cistus Incanus Flower/Leaf/Stem Extract, Commiphora Myrrha Oil, Olea Europaea (Olive) Fruit Oil*, Rosa Damascena Flower Oil*, Boswellia Carterii Oil*, Triticum Vulgare (Wheat) Germ Oil, Panthenol, Sodium Hyaluronate, Tocopherol, Tocopheryl Acetate, Sigesbeckia Orientalis Extract, Rabdosia Rubescens Extract, Gynostemma Pentaphyllum Leaf/Stem Extract, Helianthus Annuus (Sunflower) Seed Oil*, Glyceryl Linoleate, Glyceryl Linolenate, Sorbitan Palmitate, Cetyl Palmitate, Bisabolol, Lecithin, Glycine, Alanine, Serine, Valine, Threonine, Isoleucine, Proline, Phenylalanine, Histidine, Hydroxypropyl Cyclodextrin, Arginine, Allantoin, Disodium EDTA, Ethylhexylglycerin, Glutamine, Ascorbyl Tetraisopalmitate, PEG-100 Stearate, Citric Acid, Aspartic Acid, Sorbitan Olivate, Pullulan, Xanthan Gum, Decyl Glucoside, PCA, Phytoecdysteroids, Sodium PCA, Sodium Lactate, Sodium Stearoyl Lactylate, Citronellyl Methylcrotonate, Caprylyl Glycol, Cetearyl Alcohol, Phenethyl Alcohol, Phenoxyethanol, Parfum/Fragrance, Benzyl Salicylate, Linalool, Limonene, Citronellol, Geraniol, Alpha-Isomethyl Ionone, Hydroxycitronellal.<br /><br />*Organic cultivation<br />**Rosa Canina Fruit* Aqueous Infusion=Wild Rose Infusion<br /><br />The list of ingredients may be subject to change. We advise you to always check the ingredient list shown on the product purchased."
 'It takes a small squeeze of product and I can apply it all over my face and my neck area. You can feel the moisture immediately.'
 'Unfortunately, you just can judge how a shade will look on your skin until you can see the foundation against your skin. That is the reason I have been having to get more than just two shades at a time. This product comes with two different shades, but they are for people lighter than me and I am pretty pale.'
 'Instead, I would say it is foundation. I like that it has sunscreen in it. It also comes with an extra bottle of foundation and two sponges for application. Last night, after this came in, I tried some of the color on my hand. I am old so I have age spots. None were covered. But that is okay. I also discovered I should have gone a shade darker.'
 'I have seen many kits that do not include ink. Buy your own ink because the ones that have had ink are small containers. So, instead of gigging it for not having ink, review it on its performance and all that comes with it. Most beginners learn either from a tattoo artist, or from a course. There are even videos available on the internet to help you learn some things. This kit comes with 1 PC tattoo pen machine, 1 PC cable, 1 tattoo power supply and power cord, 20 tattoo needles/box, 2 bandages, 100 mixed size tattoo ink caps, 1 pedal Plate (without ink) and a piece of practice skin.'
 'This type of halo is fashioned to be secured in place with the clips. You will most likely require someone to help you the first time. Make sure to follow all directions for care so that the hair will last longer and not tangle as easy.'
 'The girl has gotten into wearing wigs. She even names them. She has a few and she makes tic toc videos to show them. Yes, she is a weird young teen. She also does up her face and nails and she does a great job. She is going to love the lavender one and the ombre one. Heck, she may even love the black one. I like that one.'
 "Burt's Bees is great for babies, children and adults. It is a nice kit and it is filled with:  Ultra gentle lotion, bubble bath, foaming shampoo and wash, nourishing baby oil, and face and Hand cloths. This can be used on anyone."
 'This travel set has an activating exfoliating cleanser and mask, a bottle of toning goodness, eye serum and a whipped moisturizer. This is what I am taking on vacation with me. I do not like packing up a lot of products that are full sized. This is great for me and my skin.'
 'This kit has a foundation that is liquid, a wooden handled short brush, a bottle of pore invisible facial primer and tops it off with a container of CC cream.'
 'This kit includes 7 sponges with different sizes, two bottles of foundation (that way you can custom blend the foundation color that will more closely match your skin). You also get a brush, if that is what you prefer to use to apply foundation. Finally, you get a small bottle of all matte pore invisible primer.'
 "Starting the treatment today also. I will use it and hopefully see results. This tool kind of resurfaces your skin and the heat helps to produce collagen. I will give it time and if it doesn't do anything, I will update"
 'Cucumber and aloe gives you such a refreshing smell. That smell can also make you feel better, The body wash is easy to use and after you lather up, you rinse. It leaves your skin moisturized.'
 'I have been known to use them on my skin and on my hair. I am a woman, but I love this scent. I burn incense with a similar scent. For my hair, I let the balm sit in my palm until it melts it enough to be liquid. Then I put it on the ends of my hair and work it up to about my ears, because the top of my hair is never getting tangled like the rest.'
 'As you age, your skin starts hanging, just like the girls do, and you will want to use products to prevent that sagging skin. This is a set that offers you anti-wrinkling and whitening in the ampoule serum, repair skin softener and repair lifting cream. This is a great starter size.'
 'I use so many products that give me moisture. I think I am addicted to them. What I know, is that from using this Celimax product and another one that I use, my face keeps moisture in it and that helps keep wrinkles from showing (which is where the hyaluronic acid comes in)'
 'these cloths are pre-moistened with coconut oil so that you can use them on the most sensitive skin. You get 12 packs with 40 cloths in each pack. That equals out to 480 cloths.  Nice for traveling, Make sure you read all disposal instructions.'
 'I am impressed. If you have sensitive skin, this is a great product for you. I have dry skin that also has eczema and sometimes rosacea. This does not aggravate either of the conditions and I really like that it is a barrier cream. That helps my skin retain moisture.'
 "This moisturizer, Tula Probiotic Skin Care, is the right consistency for day and/or night. It was nice applying the product and your face feels dewy moist.  This is much more preferable than feeling dry, oily or sticky. The scent is strongest when you open and apply. Then it softens and you can barely smell the scent. The ingredients list the scent as parfum/perfume, so you don't know exactly what it is."
 'This is a 3 piece mini set that includes Universal C Skin Refiner, Universal Pro Bio Moisture Boost Cream, Universal Moisture Essence. When you use these products, you will have moisturized skin all day long and you will reap the benefits of rejuvenated, nourished skin.'
 'This is a bubbling mask. If you have ever used one, you know already that when you put it on, it starts bubbling. This one starts bubbling after you have wet your face and then applied. The bubbling mask is great for cleaning your pores and it is also fun.'
 "before I can make a decision about how effective they are. As with most facial products, you don't see results immediately (unless it is one of those eye products that smooth and reduce puffiness under your eyes). I will use these daily until they are gone and change my review if necessary."
 'The girl needs more dip colors, so she will get this set. It comes with eight dip colors, tools for cuticles and for filing, and it also comes with a base coat, an activator, top coat, liquid brush cleaner for the base coat, activator and top coat and a nice nail brush to brush off excess dip powder. .'
 'These are so pretty. The glittery look is great - especially for younger women. Personally, I like the marbled colors. So, the girl and I will split this set up and she can have the colors that are more age appropriate for her and I will have the colors more age appropriate for me.'
 'So, to try this out, I followed the directions, opened the LED part and removed the blue battery saver paper. Then I reassembled, making sure that the batteries were in the correct position. Then, I could not get the thing to turn on. I tried in different parts of my face, holding it there and nothing happened.'
 'This product is a thicker than normal cream - but when you get some out, it is similar to a balm - without the instant melt of a balm. This spreads easily over your face. Got to say I like it. I put it over some other products I had tried. This is the winner.'
 "Because of anti depressants I take, my eyes are typically dry and I have to use moisturizing drops. If a speck of dust or a piece of hair gets near my eyes, it feels like it is scratching my eyeball. So this is a blessing for my eyes. I spend a bit of time each evening wearing this. You do have to connect it to power, but that isn't an issue for me."
 'I will probably give them to the girl. She is big in the winged liner and she does a great job. To add the eyelashes will be a snap for her. I would most likely need someone to assist me. Old age does not make it easier doing special things like lashes and liners.'
 'This is a human hair wig made for women of color. They have used wigs for years and no how to color them and curl and straighten the hair properly. I will not be using it as a wig for me. I will be using it to make wigs for some of my valuable dolls so they can have a new look.'
 "To me, it smells like it isn't fresh. It might be the shea butter or one of the oils or some other mystery ingredient. When you use it and wipe it off, it makes your lips feel dry and you will definitely need a lip moisturizer or lip mask."
 'I like that this has floating ceramic tourmaline plates. I also like that it has a fast heat up. And I like that it has the recommended heat level for different types of hair. I especially like the automatic shut off after 60 minutes and the easy restart.'
 "Doesn't matter if they are a gel, spray, cream or whatever way delivered. They work great and your skin will appreciate being moisturized all day long. This helps repair your skin to and reduce wrinkles."
 "In my guest bathroom, I have a nice mirror with lights, but it isn't movable and it doesn't have magnification or a change in the light to reflect white, warm and evening. This requires 4 AAA batteries. But it also comes with a charging cord, so you can put that in a USB outlet or charger and not use the batteries at all."
 'This facial cream can be used in the morning and in the evening. Thankfully, the instructions for English are on the web site. DAY Care- Apply adequate amount on clean skin. Pat gently to absorb.<br />NIGHT Care (Recommended for 2-3 times per week)<br />- Apply on clean face and neck. Pat gently to absorb, then apply another layer. Leave overnight.<br />I love how this feels on my skin.'
 'For those that are wanting to dip their fingers and toes into something different, this is a good starter kit. It comes with enough poly gel nail builder, that you can try different ways and colors to determine if this is something for you.'
 'In the nicely packaged box, you get a brightening cleanser, a brightening toner, a brightening lotion, a brightening cream, a brightening eye cream and a brightening essence. The products are meant to be used together and you use them as instructed. The instructions are all in Chinese, so what they did for use who can only speak English, they have attached instructions in English on the back of the packaging. The box has shrink wrap so you are able to pull the directions away from the clear wrap and put it on your box. Hopefully, you do a better job and putting it on than I did. But it works.'
 'and am leaving it on overnight. With the other product I am wearing overnight, my face feels so dewy and so soft. I like it.'
 'They are so relaxing and you can leave them on longer than you can a mask. I like to put mine in the refrigerator so that they are even more soothing. Try it.'
 'This time, I am trying three different items. I am trying the Virtue cream for you neck and décolletage, the Silk moisturizing cream and the Bright lifting eye cream. Because I put other products on my face and eye area earlier, I am putting this on my hands and arm. I love the feel of the Silk moisturizing cream, the Virtue cream is thicker than your other moisturizers, and the eye lifting cream. The eye lifting cream is applied in dots so you only go around your eye area. The Silk moisturizing cream is really nice and can be used on your face daily.'
 'I get the girl gel nails, poly nails, acrylic, you name it and all the bells and whistles. She got some last year, but they were only the gel nails and she has requested the other types and a more powerful LED/UL curing light to make things go faster. I have gotten her the sets like this, the decorative pieces and much more.'
 'I have used other Easydew products and most I like. I like this one. It goes on easy and is absorbed quickly. If it makes my skin look better, I am all in.'
 'When I first put it on my face, it felt so thick and I started thinking this was going to be way to thick and heavy feeling But it is absorbing into my skin quite well. The product is unscented but the natural scent of the oil kind of smells like old olive oil. But that smell goes away too.'
 'When you use the cushioning color control, you get skin protection, color coverage, color correction and hydration. It feels nice going on your face and keeps your face hydrated. Good stuff.'
 'But once it did prime, it let enough out to work on my eyes this morning. It felt cool thanks to metal eye roller. My eyes looked better and felt moisturized for hours.'
 'the girl, her mom and I all do our own nails. We started out with curing lamps that took a while to cure. Now we want bigger, better and faster. We got it. I would recommend  a stronger lamp for any home user.'
 "my face is soft and doesn't feel greasy, but feels moisturized. This was my mid day application of a face serum or cream. I like the facial oils. They are always nice and require only drops."
 'I have been trying several different products from this company. Now, this is an emulsion that is used to moisturize day and night. I have already moisturized my face. I have to say this is not as good smelling as the other products I have used from this company, but it does have good, natural ingredients.'
 'It smells so darn good. You will enjoy applying it to your face. It is specifically beneficial to lips, forehead, eyes, and nose to help fight aging. At my age, I applied it on my entire face and specifically on the areas specified.'
 'I have dry skin, unless I use moisturizers daily. I have been using this product a few times daily, just to keep my face moisturized. It feels good going on.'
 "She will be happy to have several didn't colors to join the set I already have for her. The colors are pretty. Make sure you follow all directions. I have not used poly gels before, so I will have her read the directions carefully. She will love the additional colors."
]
text = ' '.join(all_headlines)

# Split data into input-output pairs
max_length = 100
steps = 5
sentences = []
next_sentences = []

for i in range(0, len(text) - max_length, steps):
    sentences.append(text[i: i + max_length])
    next_sentences.append(text[i + max_length: i + max_length + steps])

# Load T5 tokenizer and model
tokenizer = T5Tokenizer.from_pretrained("t5-small")
model = T5ForConditionalGeneration.from_pretrained("t5-small")

# Preprocess data
inputs = tokenizer(sentences, return_tensors="pt", padding=True, truncation=True, max_length=max_length)
targets = tokenizer(next_sentences, return_tensors="pt", padding=True, truncation=True, max_length=steps)

# Optimizer
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)

# Training parameters
num_epochs = 3
batch_size = 16

# Track training time
start_time = time.time()

for epoch in range(num_epochs):
    model.train()
    epoch_loss = 0
    epoch_start = time.time()

    # Mini-batch training
    for i in range(0, len(sentences), batch_size):
        input_batch = {key: val[i: i + batch_size] for key, val in inputs.items()}
        target_batch = {key: val[i: i + batch_size] for key, val in targets.items()}

        optimizer.zero_grad()
        outputs = model(input_ids=input_batch['input_ids'], attention_mask=input_batch['attention_mask'],
                        labels=target_batch['input_ids'])
        loss = outputs.loss
        loss.backward()
        optimizer.step()

        epoch_loss += loss.item()

    # Calculate perplexity
    perplexity = math.exp(epoch_loss / len(sentences))
    epoch_time = time.time() - epoch_start
    print(
        f"Epoch {epoch + 1}/{num_epochs}, Loss: {epoch_loss / len(sentences):.4f}, Perplexity: {perplexity:.4f}, Time: {epoch_time:.2f} seconds")

total_time = time.time() - start_time
print(f"Total training time: {total_time:.2f} seconds")


# Validation function
# def evaluate_validation_set(model, validation_data):
#     model.eval()
#     bleu_scores = []
#     for input_text, target_text in validation_data:
#         input_ids = tokenizer(input_text, return_tensors="pt", truncation=True, max_length=max_length).input_ids
#         outputs = model.generate(input_ids, max_length=max_length, num_beams=5, early_stopping=True)
#         generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
#
#         # Compute BLEU score
#         bleu_score = sentence_bleu([target_text.split()], generated_text.split())
#         bleu_scores.append(bleu_score)
#         print(f"Input: {input_text}\nTarget: {target_text}\nGenerated: {generated_text}\nBLEU: {bleu_score:.4f}\n")
#
#     avg_bleu = sum(bleu_scores) / len(bleu_scores)
#     print(f"Average BLEU score: {avg_bleu:.4f}")
#     return avg_bleu
#
#
# # Example validation data
# validation_data = [
#     ("This moisturizer is", "great for keeping your skin hydrated."),
#     ("It smells so good", "and feels amazing on the skin.")
# ]
#
# # Evaluate model on validation set
# evaluate_validation_set(model, validation_data)


# Text generation function
def generate_text(prompt, max_length=200):
    model.eval()
    input_ids = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=max_length).input_ids
    outputs = model.generate(input_ids, max_length=max_length, num_beams=5, early_stopping=True)
    return tokenizer.decode(outputs[0], skip_special_tokens=True)


# Generate text from a prompt
prompt = "This moisturizer is great because"
print("Generated Text:")
print(generate_text(prompt))

#Hello