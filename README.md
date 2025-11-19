contextual-based-product-description-generation-using-Amazon-dataset
Field Type Explanation rating float Rating of the product (from 1.0 to 5.0). title str Title of the user review. text str Text body of the user review. images list Images that users post after they have received the product. Each image has different sizes (small, medium, large), represented by the small_image_url, medium_image_url, and large_image_url respectively. asin str ID of the product. parent_asin str Parent ID of the product. Note: Products with different colors, styles, sizes usually belong to the same parent ID. The “asin” in previous Amazon datasets is actually parent ID. Please use parent ID to find product meta. user_id str ID of the reviewer timestamp int Time of the review (unix time) verified_purchase bool User purchase verification helpful_vote int Helpful votes of the review

Product Description Model Inputs: Product Details: Essential attributes such as features, specifications, intended use, brand, and aesthetic qualities. User Reviews: A summary of user feedback, including strengths, common positive themes, noted drawbacks, and overall satisfaction level. Outputs: A structured, customer-centric description that combines technical details with real user experiences, making the product more relatable and informative.

Template Structure

Opening Sentence: Introduction & Unique Selling Proposition (USP)
Example: "The [Product Name] by [Brand] brings [unique value or feature], designed for [target audience or intended use]." 2. Key Features Overview: Highlight Core Specifications

Example: "With [feature 1], [feature 2], and [feature 3], this product offers [summary of benefits, like 'seamless performance and durability']. Its [design element or material] provides both a modern aesthetic and added durability." 3. User Experience Summary: Positive Feedback

Example: "Users consistently appreciate [feature users like, e.g., 'its lightweight build and ergonomic design'], noting that it [specific positive outcome, like 'enhances comfort during extended use']. Many also mention its [feature], which has proven to be [benefit, like 'reliable and efficient in various conditions']." 4. Addressing Drawbacks (If Any)

Example: "While a few users mentioned [minor drawback, like 'the battery could last longer'], most agree that this doesn't detract significantly from the product's overall performance." 5. Conclusion: Final Recommendation or Customer Satisfaction Summary

Example: "Overall, the [Product Name] has earned high marks for its [positive attributes, like 'functionality and style'], making it a top choice for those seeking [intended use or product category]. With an average rating of [rating/5], it’s clear this product meets user expectations for [key value]." Example Using the Model Product: XYZ Smart Thermostat

Product Details:

Primary Features: Energy-efficient, remote control via app, easy installation Brand Information: Known for eco-friendly, innovative products Intended Use: Home climate control Technical Specifications: Works with Alexa/Google Assistant, real-time temperature adjustments Aesthetic Qualities: Sleek, minimalist design in black or white User Reviews Summary:

Strengths: Easy setup, responsive controls, energy savings Common Feedback: High user satisfaction, saves on bills, intuitive app Drawbacks: Initial setup may be tricky for non-tech users Overall Sentiment: Highly recommended, with an average rating of 4.7/5
