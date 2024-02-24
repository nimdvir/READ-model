Sticky Words: A Computational Linguistics Approach to Assessment and Manipulation of Information Engagement

**Nim Dvir**

#   {#section .unnumbered}

#  {#section-1 .unnumbered}

# Abstract {#abstract .unnumbered}

With increasing amounts of digital information being published by government, business, organizations, and individuals, understanding how digital information can be presented to improve user experience (UX) has gained increasing importance. *Information engagement* (IE) is an especially important aspect of UX reflecting behavioral, emotional, and cognitive responses to digital information*.* While the significance of IE has been well documented, little research has investigated how to systematically measure it; design for it; and, most importantly, improve it.

This dissertation work developed and empirically validated a novel framework for assessment, prediction, and manipulation of IE based on the phrasing of the information itself. The objectives were to a) conceptually and operationally define IE; b) identify textual features of engaging information; and c) develop a method and instrument for systematic prediction and manipulation of IE using computational linguistics, text analysis, and natural language processing. These objectives were fulfilled within three research phases. In Phase 1, a conceptual model of IE dimensions and determinants was developed through a comprehensive interdisciplinary literature synthesis and empirically validated using large-scale user surveys. In Phase 2, a set of engaging textual attributes were identified to inform development of a method and instrument for the assessment and manipulation of IE using computational linguistics. In Phase 3, the IE model, method, and instrument were empirically tested to confirm that they improved IE with textual information.

This research into the importance of word choice on UX contributes to the literature in several respects. Its identification of quantitative textual attributes that can be used to measure and predict engaging words and then applying them to construct and validate a systematic and automatic method for assessment and improvement of IE contributes an important tool and methods for immediate evaluation of IE and for further research into how to improve it. Their further application to diverse domains may identify ways to greatly improve IE, and therefore UX, with various media.

# Introduction 

## Problem definition

*Information* is the meaning of data \[@zins2007\]. [^1]The key characteristic of information is that it is subject to interpretation and processing. Data is being processed into information and then interpreted into knowledge \[@fricke2009\]. In written or digital text, each symbol, letter, word, phrase and so on convey information. The data available at one level is processed into information to be interpreted at the next level, until the information at the top level is interpreted and becomes knowledge. Information, therefore, is not knowledge itself, but rather the representation of it.

*Communication* is the exchange of information, or the act of conveying meaning. Providing information in the best form and format is critical to the success of information systems (IS) (Delone & McLean, 2003). Traditionally, IS research has been focused on the efficiency and effectiveness of information delivery and design. However, current research has been increasingly concentrated on the importance of *user experience* (UX), which encompasses all aspects of the end-user\'s interactions with a company, its services, and its products (Venkatesh & Bala, 2008; ISO 9241, 2019). In recent years, the term *engagement* has been increasingly used to describe and measure the quality and depth of UX \[@obrien2020\]. Referring to the emotional, cognitive, and behavioral connection between a user and a technological resource at a point in time and possibly over time \[@attfield2011; \@obrien2016d\], engagement emphasizes the positive aspects of interacting with a system and, in particular, the desire to use it longer and repeatedly \[@lalmas2014\].

This study focuses on assessment and improvement of *Information Engagement* (IE), defined as a measure of how users interact with information, and how it is expressed by the system. Long identified as a goal of organizational communication and a critical driver of successful information interactions, IE reflects the quality of the connection between users and the information and can affect the overall customer experience both online and offline \[@akdeniz2013; \@brodie2013; \@singh2010\].

Of the various means by which information can be communicated, this research focuses on IE with digital text. The study is motivated by current changes to the delivery and design of digital text, and the problems that arise when it is not engaging. Increasing reliance on computer-mediated communication (CMC) and information and communication technologies (ICT) has transformed how digital information is expressed, experienced, exchanged, and employed. Currently (in 2022) the majority of the information distributed digitally continues to be in the form of text \[@johnston2018b\]. Recent studies have found that 93% of adults in the United States have consumed textual information online, either via a mobile device or a computer \[@stocking2017\]; 79% have made an online purchase, spending nearly \$350 billion annually as a nation \[@smith2017\]; 80% of have accessed at least one online government service \[@chan2008; \@grimmelikhuijsen2013; \@im2013\]; and 71% have searched online for health information \[@imlawi2017; \@kostkova2016; \@perski2017; \@rockhealth2015\].

With increasing amounts of digital information being published by commercial businesses, governments, healthcare organizations, and private citizens, the competition for attention and interest is constantly growing. With increasing theoretical and empirical evidence of its positive impact on education, government, and business (Arapakis, Lalmas, Cambazoglu, et al., 2014; R. Jacques et al., 1995; Oh & Sundar, 2016), IE is considered a significant factor in information delivery. Initiating, sustaining, and improving engagement can result in positive outcomes for citizen inquiry and participation, e-health, web searching, and e-learning \[@huang2019; \@obrien2016d\]. It has become a goal---and to some extent, a necessity---of user interactions in various information-rich contexts and domains, including government, education, marketing, and healthcare \[@feng2015; \@frick2010; \@huang2019; \@lagun2016; \@lalmas2014\]. Alternatively, failure to create IE often leads to lack of attention, involvement, and investment, and is associated with diminished productivity and poor decision-making \[@chen2009; \@lagun2016; \@obrien2020; \@obrien2016d; \@soto-acosta2014\]. Despite the significance of IE, many organizations fail to achieve it, resulting in their online information being barely read and quickly forgotten \[@arapakis2017; \@nielsen2015; \@szabo2008\].

In terms of design, IE has been proposed as a useful metric for assessing information quality and, by extension, the effectiveness of the information-management strategies of organizations \[@bardus2016; \@eppler2006; \@jiang2016\]. In accordance, the Advertising Research Foundation (ARF) affirmed that engagement is "the 21st century metric of marketing communication's efficiency and effectiveness,\" representing anything that can stimulate the level of viewers' attention and emotion \[@plummer2006a\]. As information quality is a critical factor in information system success, developing a means of its assessment is essential \[@delone1992; \@delone2003\].

Recent developments in computational linguistics and natural language processing (NLP) have created opportunities to explore systematic, computational, and automatic approaches to the evaluation, creation, and improvement of digital text \[@dvir2019d\]. While designing for engaging experiences is an oft-cited goal of interactive-system developers in many disciplines, they have few guidelines for creating engaging information \[@blythe2005; \@overbeeke2003\]. Moreover, little research is focused on the development of IE, resulting in a lack of systematic and computational approaches for its initiation, sustainment, and improvement of IE \[@obrien2017; \@obrien2016d\].

Resolving these problems requires deep understanding of the IE process; the factors that influence it; and how it can be predicted and developed strategically, systematically, and computationally \[@lalmas2014; \@obrien2016d\].

## Objectives and goals

The overarching objective of this dissertation was to improve the delivery and design of digital textual information. Its specific aim was to develop and validate a descriptive, predictive, and prescriptive framework for IE measurement and manipulation. Achieving this aim required fulfillment of the following goals:

1.  Conceptually and operationally define IE by identifying its distinctive dimensions and determinants

2.  Identify attributes of engaging information and apply them for quantitative feature selection

3.  Develop a predictive model

4.  Create and test an instrument to assess and manipulate IE systematically and computationally using computational linguistics, text analysis, and NLP.

Achieving these goals required addressing the following research questions:

**R~1~: What are the definitions, dimensions, and determinants of IE?**

**R~2~: Can IE be predicted systematically and computationally based on textual features?**

**R~3~: Can IE be manipulated systematically and computationally using computational linguistics and NLP?**

These questions were addressed in three research phases.

**[Phase I (Chapter 2)]{.underline}** conceptually and operationally defined IE and its unique dimensions and determinants. The findings were used to develop a new measurement model that emphasizes the influence of word choice (phrasing) on IE and supports its significance as a research topic.

**[Phase II (Chapter 3)]{.underline}** developed a model and method to evaluate and predict IE. Applying behavioral economics research, particularly Cumulative Prospect Theory (CPT), predictive IE attributes were identified and mapped to quantifiable and measurable textual features that were empirically validated as significant predictors.

**[Phase III (Chapter 4)]{.underline}** drew upon embodied cognition and the framing effect to develop and validate a prescriptive model and method to improve IE based on word substitution.

The findings of these three phases contributed to the development and validation of (1) an original definition and measurement model for IE, (2) a set of features useful for predicting and developing IE, and (3) a method of IE assessment and manipulation using computational linguistics.

The following chapters describe the three research phases in detail.

# Definition, Dimensions, and Determinants of Information Engagement

## Introduction

Phase I explored the dimensions and drivers of IE, focusing on the influence of textual information. First, a comprehensive, interdisciplinary literature synthesis was conducted to define IE, describe how it is manifested (i.e., its attributes), and identify its determinants. At the same time, two theoretical models, *User Engagement Theory* (UET) and *Information Behavior Theory* (IBT), were reviewed and unified for application to the information model. Synthesizing the theoretical models and the related literature allowed for development of a model illustrating how IE is manifested, differs from other forms of engagement, and is driven and fostered by the information itself. Finally, the model was empirically validated in a large-scale user study measuring the dimensions of IE.

## Literature review

### Definitions

The definition of *engagement* varies by the domains in which it is a factor. In the domains of government and public policy, the terms *civic engagement* and *political engagement* indicate positive participation in the political process \[@abbas2010a; \@chan2008; \@dvir2017b; \@grimmelikhuijsen2013; \@gutman1982\]. In business and marketing, *consumer engagement* and *customer engagement* are used to describe consumer relationships with a company or brand \[@batra1986; \@brodie2013; \@rowley2008; \@zheng2015\]. In the digital domain, *engagement* is the connection between an external stakeholder (a consumer) and an organization (a company or brand) through various channels. The results of this connection can affect a specific aspect of the customer experience or the overall customer experience, either offline or online \[@akdeniz2013; \@brodie2013; \@singh2010\].

As a quality of an information system, engagement explains how and why information attracts users \[@sutcliffe2016\]. Measurement of engagement has been proposed as a useful means of assessing the effectiveness and success of the information-management strategies of organizations (Jiang et al., 2016; Paine, 2011). Research into organizational communication often assumes that if IE is occurring, it is positive and desired \[@depaula2018; \@dhanesh2017\], For example, in the context of government and public policy, IE is believed to indicate positive participation in the political process \[@abbas2010a; \@chan2008; \@dvir2017b; \@grimmelikhuijsen2013; \@gutman1982\]. []{dir="rtl"}In a study of communication during the first months of the COVID-19 epidemic in the United States, IE proved important in message diffusion (transmission and retransmission), resulting in amplification of messages in the social media environment \[@sutton2020\].

Table 1 summarizes the major definitions of IE.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Definition**                                                                                                                                                                                                                                                                             **Source**                                    
  ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ --------------------------------------------- ------
  A state of emotional involvement or commitment and a process of drawing favorable attention and interest                                                                                                                                                                                   \[@2020\]                                     

  The level of user involvement with a product; the frequency, intensity, or depth of interaction between a user and a product, feature, or service over a given period; an unbiased behavioral measurement that is trustworthy, valid, and reliable.                                        \[@sharon2018\]                               

  The emotional, cognitive, and behavioral connection that exists, at any point in time and possibly over time, between a user and a resource                                                                                                                                                \[@attfield2011\]                             

  Quality of the user experience that emphasizes the positive aspects of interacting with an online application and, in particular, the desire to use that application longer and repeatedly                                                                                                 \[@lalmas2014\]                               

  The state of mind that must be attained to enjoy a representation of an action                                                                                                                                                                                                             \[@laurel2014, p. 116\]                       

  Users' response to an interaction that gains, maintains, and encourages their attention, particularly when they are intrinsically motivated                                                                                                                                                \[@jacques1996, p. 103\]                      

  Users' investment of time, attention, and emotion in an interaction with information                                                                                                                                                                                                       \[@frick2010\]                                

  A combination of people's views toward new information and their appetites for it                                                                                                                                                                                                          \[@horrigan2017\]                             

  A business communication connection between an external stakeholder (consumer) and an organization (company or brand) through various channels of correspondence, manifested as a reaction, interaction, effect, or the overall customer experience that takes place online and offline.   \[@akdeniz2013; \@brodie2013; \@singh2010\]   

  A metric of marketing communication efficiency and effectiveness that represents anything that can stimulate the level of attention and emotion                                                                                                                                            \[@plummer2006a\]                             
  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : . Definitions of Information Engagement

In this dissertation we present a more overarching definition of IE, IE which refers to both the users, as the quality of their reaction to information that is manifested as affective, behavioral, and cognitive investment and involvement when the user interacts with information, and the system itself, referring to how the information is expressed by the system.

## Literature review

Engagement studies in various areas suggest that by increasing engagement with textual information, institutions can positively and significantly affect outcomes \[@obrien2020\]. However, determining how to do so is challenging because digital information attracts users for different reasons \[@obrien2016e\]. Table 1 summarizes the desired IE goals and attributes in various research domains.

Table 1. IE Goals and Attributes Research Domains

+------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Domains**                  | **Goals and Attributes**                                                                             | **Sources**                                                                                                                                                                                                                                                                                                                         |
+==============================+======================================================================================================+=====================================================================================================================================================================================================================================================================================================================================+
| **Public policy, health,**   | Creating knowledge, informing users, increasing number of users                                      | \[@bahry2015; \@chan2008; \@grimmelikhuijsen2013; \@huang2019; \@martin2016a; \@navajas2014a; \@stewart2009\] \[\[CSL STYLE ERROR: reference with no printed form.\]; \@chan2008; \@kostkova2016\]                                                                                                                                  |
|                              |                                                                                                      |                                                                                                                                                                                                                                                                                                                                     |
| **and government**           |                                                                                                      |                                                                                                                                                                                                                                                                                                                                     |
+------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
|                              | ,                                                                                                    | \[@hagen2016\] \[@perski2017\]                                                                                                                                                                                                                                                                                                      |
+------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Education**                | Stimulating desire to learn; being                                                                   | \[@abraham2019; \@appleton2008; \@bomia1997; \@denoyelles2015; \@dincelli2020; \@fredricks2004; \@guerini2012; \@newmann1992; \@so2008\]                                                                                                                                                                                            |
|                              |                                                                                                      |                                                                                                                                                                                                                                                                                                                                     |
|                              | novel, relevant, current, and easily sharable                                                        |                                                                                                                                                                                                                                                                                                                                     |
+------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Marketing and e-commerce** | Stimulating loyalty, satisfaction, empowerment, connection, emotional bonding, trust, and commitment | \[@koufaris2002; \@oestreicher-singer2012\] \[@batra1986; \@brodie2013; \@brodie2011a; \@google2013\].                                                                                                                                                                                                                              |
+------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **Media and gaming**         | Increasing level of focused attention, affect, and interest                                          | \[@aranyi2015; \@arapakis2017; \@arapakis2014a; \@barthel2016; \@bialik2017; \@legg2014a; \@lopez2012; \@loureiro2011; \@mitchelstein2010; \@nielsen2009; \@obrien2011; \@obrien2017a; \@obrien2016e; \@obrien2014; \@reis2015; \@schmidt2017; \@stroud2015\] \[@blythe2003; \@boyle2012; \@cairns2016; \@mekler2014; \@wiebe2014\] |
+------------------------------+------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

: . Dimensions of Information Engagement

Overall, IE manifests as the stimulation and maintenance of user interest, motivation, and attention and correlates with feelings of enjoyment and immersion in the experience. However, there is no agreement on which information features are stable and controllable determinants of IE. This research gap prevents systematic employment of data analysis, statistical calculation, computational linguistics, and NLP to improve the design of information to increase IE.

As data collection and computational capacity increase, an increasing number of techniques and programs to evaluate and develop IE systematically or even automatically become available. *Text data mining* (TDM), roughly equivalent to text analytics, is the process of deriving high-quality information from text \[@hearst1999\]. With increasing access to intuitive human-machine interfaces and databases, language computation and processing have come to play a central role \[@bird2019\].

It is estimated that around 80% of all information is unstructured, much of it in the form of text in social media, email, texts, webpages, and online platforms. Although text can be an extremely rich source of information, analyzing, understanding, organizing, and sorting unstructured textual data is difficult and time-consuming, so most companies fail to tap its full potential \[@kodagoda2016\]. In contrast, machine learning applications can automatically analyze millions of text data sources at a fraction of the cost and time. Using scalable text-classification tools, companies can automatically structure all manner of text rapidly and cost-effectively, allowing them to save time, automate business processes, and make data-driven business decisions.

Recent developments in text classification have provided new opportunities for systematic word selection. *Text classification*, the process of assigning tags or categories to text according to its content, is one of the fundamental tasks in NLP. A field within artificial intelligence (AI) and machine learning that combines linguistics and computer science to break down language for analysis by machines, NLP has broad applications, such as sentiment analysis, topic labeling, spam detection, and intent detection.

### Dimensions of Information Engagement

According to a review of IE in various domains, three primary dimensions are generally recognized: *perception, participation*, and *perseverance.* This section describes how IE manifests in these three dimensions, including as (a) level of interest in and intent for the information (i.e., affect regarding, attitude toward, perception of, and evaluation of the information that users develop) (b) interaction with the information (i.e., action or participation in the information exchange), and (c) integration of the information (i.e., perseverance using and employment of the information).

#### IE as perception {#ie-as-perception .unnumbered}

As *engagement* is defined as the state of emotional involvement and commitment produced by the process of attracting and engaging user interest \[@2020\], IE can be described as a quality of user experience (UX) that measures how the information is experienced by the user. As a subjective evaluation,‎ IE reflects a user\'s emotions and attitudes toward the information \[@hassenzahl2006\], emphasizing the phenomena attracting users toward the information and thereby motivating them to interact with and use it \[@attfield2011; \@obrien2008a\]. Therefore, IE as perception can be conceptualized as the relationship between users and the information that manifests as the level of motivation, interest, and intention toward the information, as well as an affective dimension that pertains to the quality and depth of UX with information \[@obrien2011; \@obrien2008a\]. IE is related to *affective involvement* or *enduring involvement,* a concept that explains why consumers, rather than becoming bored, become increasingly connected to and involved with a product over time \[@bloch2009a; \@commuri2008\].

IE can be divided into *hedonic* and *utilitarian* IE \[@obrien2010a\]. Hedonic IE is often associated with gratification, enjoyment, and interest, phenomena often seen in leisure-based settings, such as gaming, social media, and reading online news. In such settings, IE manifests as stimulation and maintenance of user interest, motivation, and attention and correlates to feelings of enjoyment and immersion in the experience \[@blythe2003; \@boyle2012; \@cairns2016; \@mekler2014; \@wiebe2014\]. In contrast, utilitarian IE is associated with fulfilment of values and goals by a system and interaction at different points in time \[@nevo2016\] and is motivated by the need to obtain digital information for important matters, such as health, education, finance, employment, and government services \[@begany2017; \@dvir2017b; \@kostkova2016; \@rainie2007\].

#### IE as participation  {#ie-as-participation .unnumbered}

IE as perception relates to the level of involvement and investment in information interactions \[@attfield2011; \@obrien2008a\]. In this context, IE is a behavioral process, a measure of the quality of participation in the information interaction that leads to information transfer or information exchange. As it involves accessing and acquiring information, IE as participation manifests as observable user actions that can be measured by behavioral metrics and may be active or passive. For example, in social media, "liking," commenting on, and sharing content are active IE measures while viewing is a passive measure \[@xu2019\].

IE as active participation has been increasingly pursued with the introduction of Web 2.0 \[@oreilly2010\], which enables two-way information flow and user-generated content \[@bruns2008\]. Active IE manifests as commenting on news articles \[\[CSL STYLE ERROR: reference with no printed form.\]\]; reacting, sharing, clicking on, or commenting on users' posts \[@facebook.com2016\]; signing and sharing political/policy petitions \[@dumas2015; \@hagen2016\]; and other forms of actively participating in digital information interactions \[@dolan2016a; \@mccay-peet2016\]. These behaviors not only transform into comparable performance metrics and quality indicators but also stimulate follow-up activities that replicate and expand on information across other channels and technologies \[@bardus2016; \@boyle2012; \@dolan2016a; \@dvir2018c; \@perski2017\]. Such activities have been used as social marketing tools to enhance visibility and extend the reach of information generally or the mission of an organization specifically \[@xu2019\].

#### IE as perseverance  {#ie-as-perseverance .unnumbered}

IE is associated with a state of awareness (consciousness) and its physical manifestations that outlive the process that created them, resulting in the adoption and use of information \[@zins2007\]. As such, it can be described as the process of information *perseverance*, a cognitive dimension that manifests as information retention, integration, and influence \[@obrien2017a; \@ritchie1996\]. IE as information retention is often associated with the desire to learn, share knowledge, and stay current with knowledge development \[@abraham2019; \@dewey1998; \@dincelli2020\] \[@appleton2008; \@bomia1997; \@chapman2003; \@chapman1999; \@cole2009; \@dvir2015a; \@guo2014; \@meece1988\].

In the education domain, IE manifests as cognitive interaction with pedagogical materials, activities, communities, and experiences \[@abraham2019; \@appleton2008; \@bomia1997; \@cole2009; \@dincelli2020; \@dvir2015a; \@meece1988\]. In the commercial domain, IE manifests as investment in information interaction and sustained attention and interest \[@obrien2008a; \@oestreicher-singer2012\].

IE as retention can also be seen as the user's level of determination to use or disposition toward information. For example, in business contexts, such as e-commerce and marketing, IE as retention is often used to describe the development of user loyalty \[@koufaris2002; \@oestreicher-singer2012\] among engaged consumers who exhibit enhanced connection, emotional bonding, trust, and commitment \[@batra1986; \@brodie2013; \@brodie2011a; \@google2013\]. This connection occurs over a period of time and is associated with adoption and recommendation of information \[@lalmas2014\].

Table 2 describes the dimensions of IE.

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Process           Dimension         Expression                                                                                                                                             Evaluation
  ----------------- ----------------- ------------------------------------------------------------------------------------------------------------------------------------------------------ ------------------------------------------------------------------------------
  Perception        Affective         Mental impression and interpretation expressed in involvement with, interest in, and intent for the information; relationship toward the information   Information experience

  Participation     Behavioral        Investment in the information interaction                                                                                                              Information exchange; retrieval and reactions to the information (selection)

  Perseverance      Cognitive         Integration and influence of the information                                                                                                           Employment and endurability (retention and decision-making)
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : . IE determinants

### Determinants of Information Engagement

IE is dependent on myriad factors relating to the task (the information interaction), the system (the technology), and the user. These factors include the user's ability to attend to and become involved in the experience and overall evaluation of the experience, as well as the system's ability to support the experience.

**User determinants** include intrinsic variables, namely demographics and personal characteristics significantly associated with IE, including age \[@perski2017\], gender \[@boyle2012; \@dvir2015a; \@johnson2011; \@ma2011\], prior knowledge, personal relevance \[@arapakis2014a\], and technological knowledge and confidence \[@arapakis2014a; \@perski2017\].

**Task determinants** relate to the user's goals and the activities performed to accomplish them. It may appear intuitive that different tasks promote different engagement trajectories in different settings, yet this assumption has not been systematically investigated \[@obrien2020\]. The differential impacts of the intersection of task characteristics with personal motivations and goals make it challenging to determine which task attributes influence IE. Previous research has highlighted type (e.g., information-seeking or decision-making), goal (e.g., concrete or abstract), product (e.g., format or use), frequency (e.g., discrete or repetitive), impetus (e.g., self or others), and length of time required as task determinants of IE \[@obrien2020\].

Two stable task-related determinants are **interest and complexity**. Having demonstrated clear links between interest and IE \[@arapakis2014a; \@obrien2020; \@obrien2017a; \@obrien2016e\], research has shown interest to be crucial in many information domains, including online news and social media \[@arapakis2014a; \@berger2012\]. Task complexity has also been shown to drive IE, with perceived effort suggested as a barrier to IE \[@gofman2007; \@gofman2009; \@nielsen2015; \@obrien2016d\]. Much research has investigated the factors associated with task complexity, such as the number of possible paths or outcomes of a search task \[@dvir2018c\], user perceptions of task difficulty \[@willett2014\], and degree of a priori determinability or certainty inherent in the task. Research has proposed that difficulty is an attribute of IE, with UX related to whether a task is too easy, too difficult, or at just the right level of difficulty \[@chen2009; \@obrien2020; \@obrien2018a\]. The optimal level of difficulty, that at which the digital interaction is commensurate with level of knowledge and skill, is believed to contribute to positive IE. In accordance, research has highlighted the role that prior topical knowledge and skills play in task complexity \[@aranyi2015; \@arapakis2014; \@li2008\].

**System determinants** relate to features of the system that affect IE, including extent of interactivity, type of format(s), and possible uses \[@abraham2019; \@dincelli2020; \@norman2013a; \@oh2016\]. System determinants include the design of the graphical interface, in particular its saliency or "visual catchiness" \[@eisenstein2007; \@koehler2014; \@mccay-peet2016; \@uskul2010\]. Information design has been shown to facilitate product-centered interaction, suggesting that marketers can significantly influence the development of enduring product involvement \[@bloch2009a; \@commuri2008\]. This finding has long-term implications for consumer spending and behavior in relation to a product category or brand.

Another critical determinant is the design of the content itself, which encompasses the digital information (e.g., text, sound, and video) provided by the system and how it is presented, as well as additional information stemming from the medium in which the information is delivered (Gafni & Dvir, 2018; Rowley, 2008; Jarvenpaa et al., 2006; Jennings, 2000; Lee & Turban, 2001; Wells et al., 2011). Textual features have shown to predict and facilitate IE in various domains, with the amount of text having been found to influence consumers' willingness to disclose personal data \[@dvir2018c\].

Several studies have assessed information attributes using textual analysis to predict the outcomes of computational tasks relating to IE, such as predicting the memorability of movie quotes \[@cheng2012\] or the comedic level of cartoon captions \[@shahaf2015\]. Concerning specific words, the findings of computational linguistics have been used to predict popularity or frequency \[@turney2019\]. In their study, Turney and Mohammad (2019) developed a seven-step algorithm to predict the most frequently used word to convey a certain meaning, of which the first four steps combine information from WordNet and Google Books Ngram Corpus to make an integrated dataset of different words that represent the same meanings and the last three steps involving supervised learning, a type of machine learning using labeled datasets to train algorithms to classify data or predict outcomes, with feature vectors, ordered lists of numerical properties used as inputs to a machine learning model.

There have been increasing calls for emphasizing *context*, defined as "situational opportunities and constraints that affect the occurrence and meaning behavior as well as functional relationships between variables" \[@johns2006, p. 386\], and *contextual theorizing* for IS research \[@malthouse2007; \@nardi1996context; \@stockdale2006; \@venkatesh2011\]. However, there is no agreement on which contextual factors influence IE and how to design for them

In sum, IE depends on the user's internal state, including predispositions, expectations, needs, motivation, and mood; the characteristics of the designed system, including complexity, purpose, usability, and functionality; the context and environment within which the interaction occurs; and the tasks that drive the interaction.

Table 3 summarizes the major determinants of IE.

  ------------------------------------------------------------------------------------------------------------------------------------------
  Dimension       Determinants                                           Sources
  --------------- ------------------------------------------------------ -------------------------------------------------------------------
  User            Age                                                    \[@perski2017\]

                  Gender                                                 \[@boyle2012; \@dvir2015a; \@johnson2011; \@ma2011\]

                  Prior knowledge and personal relevance                 \[@arapakis2014a\]

                  Literacy or confidence                                 \[@arapakis2014a; \@perski2017\]

  Task            Goals and outcomes                                     \[@obrien2016e\]

                  Type, product, process, and time-related qualities     \[@obrien2020\]

                  Interest                                               \[@arapakis2014a; \@obrien2020; \@obrien2017a; \@obrien2016e\]

                  Complexity                                             \[@gofman2007; \@gofman2009; \@nielsen2015; \@obrien2016d\]

  System          Interactivity, formats, and uses                       \[@abraham2019; \@dincelli2020; \@norman2013a; \@oh2016\]

                  Design saliency or "visual catchiness"                 \[@eisenstein2007; \@koehler2014; \@mccay-peet2016; \@uskul2010\]

                  Amount of information                                  \[@dvir2018c\]

                  Sentiment, novelty, quality, and information framing   \[@arapakis2014a; \@mccay-peet2016; \@obrien2017\]
  ------------------------------------------------------------------------------------------------------------------------------------------

  : . Information of Behavior Theory and User Engagement Theory

## Theoretical underpinning 

The theoretical foundation on which this study bases IE draws from ‎several research areas: human-computer interaction (HCI), which focuses on user characteristics; information science, which focuses on information use; and cognitive psychology and behavioral economics, which focus on the impact of information expression. This foundation is based on the unification of two theoretical frameworks relating to the affective, behavioral, and cognitive dimensions of IE: User Engagement Theory (UET) and Information Behavior Theory \[@wilson2010; \@wilson2000; \@wilson1997; \@wilson1981\];

### User Engagement Theory (UET)

UET was developed to explain *user engagement* (UE), self-directed, meaningful involvement with technological resources \[@obrien2008a\].

UET was developed originally as a framework for technology-based teaching and learning \[@kearsley1998\]. It argues that students must be meaningfully engaged in learning activities through interaction with others and worthwhile tasks. Although engagement can occur without it, technology can facilitate engagement in ways that are difficult to achieve otherwise \[@kearsley1998\]. UE, therefore, is "a restricted explanation of UX that concentrates on judgement of product quality during interaction" \[@hart2012a\].

Current research on UET aims to expand process models of user judgement to encompass the nature of interaction as explored through affect, flow and presence; and how this inform UE (seen as a subset of UX).

See figure below (taken from Hart et al. 2012) .

![Diagram Description automatically generated](./assets/media/image1.png){width="4.21875in" height="7.1875in"}

Figure . UET

**User Engagement Process Model and Scale**

UET was used as the basis for the development of UE process model and scale. The UE conceptual model ("The Process Model of User Engagement") views UE not as a singular element but rather a process in which users move in the same trajectory when interacting with ICT as they initiate and sustain engagement with the application or task, disengage from it, and potentially re-engage once or repeatedly with it \[@obrien2008a\]. Experiential and user-based, it presents a model to explain how users judge quality according to criteria such as aesthetics, usability, and engagement \[@obrien2010; \@obrien2008a\]. The UE process model is comprised of four stages: the point of engagement, sustained engagement, disengagement, and potential re-engagement.

-   **The point of engagement** occurs when users decide to invest in an interaction and to initiate and sustain engagement in a task. It is initiated by the aesthetic appeal and novelty of the interface, interest in it, motivation to use it, or need to fulfill a specific a goal through interaction with it.

-   **A period of sustained engagement** occurs when users maintain their attention and interest in the application.

-   **Disengagement** occurs when users decide to stop using an application or when factors in the external environment cause them to cease being engaged with it.

-   **Re-engagement** occurs when users return to an application as a result of positive experience with it.

The stages of the process model correlate with the dimensions recognized in the literature review. The point of engagement relates to participation, manifested as retrieval of information and the start of information interaction and exchange, while sustained engagement and re-engagement relate to perseverance, manifested in awareness, recall, and retrieval of the information from memory.

By segmenting engagement into stages, O'Brien and Toms (2008) were able to identify attributes from previous research that appear most salient for each phase of an interaction to predict and facilitate engagement. These attributes, which pertain to the user, the system, and the user-system interaction, are based on user perception and therefore subjective \[@obrien2008a\]. O'Brien and Toms used the concept of *affordances*, the perceived and actual properties of an object that determine how a system could be used \[@norman2013a\], to develop the UES for evaluating engaging outcomes \[@obrien2018; \@obrien2010\]. As concepts within HCI, affordances are often used to describe what functions an object allows for and how it can be signaled. Based on the model, O'Brien and Toms developed the User Engagement Scale (UES), a measure of how information is experienced and related to **perception**, the third dimension described in the literature, as well as mental impression and interpretation. The original version of the UES taps into six self-reported affordances of the information experience \[@obrien2010\]. The short form UES (UES-SF) groups the original six affordances into four---aesthetic appeal (AE), perceived usability (PU), reward (RW), and focused attention (FA)---and contains 12 questions answered using a 5-point scale Likert scale ranging from 1 (strongly disagree) to 5 (strongly agree; see Appendix A).

  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Affordance                 Definition
  -------------------------- ----------------------------------------------------------------------------------------------------------------------------------------------------------
  Aesthetic appeal (AE)      Level of interest and curiosity evoked by the system and its contents and perception of the visual appearance of the computer application interface

  Focused attention (FA)     Concentration of mental activity resulting from being drawn in, interested by, and experiencing enjoyment during the interaction

  Perceived usability (PU)   Affective (e.g., frustration) and cognitive (e.g., effort) responses to the system

  Reward (RW)                Overall evaluation of the experience, its perceived success, and likelihood to return to it; relates to whether users would recommend the site to others
  -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : . The 50 synsets analyzed in the study

UES Affordances \[@obrien2018\]

Tests of the UE Process Model and the UES for reliability, validity, and generalizability in various domains, mostly leisure (e.g., online news, shopping, digital games, and social media), corroborate the model and the feasibility of using a universal measure of engagement \[@obrien2018; \@obrien2017a; \@obrien2010; \@obrien2008a; \@obrien2016d\]. The results also demonstrate that engagement is consistent across diverse types of applications in terms of the trajectory followed by users throughout the process of using them and the attributes present. The UES has been adopted by more than 50 international research teams who have used it to examine UE with educational technologies, search systems, haptic technologies, health and consumer applications, and other media \[@obrien2018; \@obrien2016d\]. The attributes identified as part of the UES were all found to be interconnected, demonstrating that the design process must consider the entire user experience rather than a single dimension.

**Limitations**

While UE Process Model and UES provide an important framework for the study of IE, they have several limitations:

-   The UE Process Model emphasizes engagement as a quality of UX and interaction with *technology* but not with *information*. Currently, IE and interaction are not well situated within the theory \[@obrien2017; \@obrien2011\]. The model and scale do not emphasize information qualities as attributes for engagement; rather, they focus primarily on the characteristics of the system and how they are perceived and acted upon by users. However, information attributes have been shown to be important factors in UE when interacting with technology \[@obrien2011; \@obrien2014\]. In their later work on the UE Process Model and UES, O'Brien et al. suggested that the UE framework be broadened to incorporate IE and for more investigation of the relationship between IE and information presentation through the interface \[@obrien2011; \@obrien2016b; \@obrien2016e; \@obrien2014\].

-   The current model and scale are focused on identifying and evaluating UE but not on the development of engaging experiences \[@obrien2017; \@obrien2016d\].

-   While the UES has been established as a reliable self-report measure of UE, it is not always applicable to IE. Self-report metrics are not always available in information environments (e.g., when users read texts on a website). Also, some of the self-reported measures in the UES are either irrelevant to textual information interactions (e.g., aesthetic appeal) or can be inaccurate (e.g., measures of focused attention) and should be studied using behavioral or cognitive metrics. Therefore, holistic approaches to evaluation that blend subjective and objective measures, as appropriate for the study of information, context, and constraints, have been recommended \[@obrien2018a\].

-   Despite general agreement that IE supports successful information tasks, such as information adoption and use, little emphasis has been placed on providing empirical evidence of it \[@obrien2020\]. Most current research is focused on studying the effects of IE on tasks in leisure and entertainment domains \[\[CSL STYLE ERROR: reference with no printed form.\]\] and little has focused on studying its effects in more pragmatic domains, such as government and health \[@bomia1997; \@chan2008; \@imlawi2017; \@kostkova2016\]**.** Further study should examine whether IE can lead to information adoption and use and how it can be measured and designed to do so.

### Information Behavior Theory

IBT contributes to the study of IE by focusing on the adoption and use of information in performing an information task to accomplish a goal Wilson, 1981, 1997, 2000). Information behavior is described as the totality of human behavior in relation to sources and channels of information, including both active and passive information-seeking, and information use \[@wilson2000; \@wilson1981\]. In the IS literature, which focuses on the adoption and usability aspects of IE \[@perski2017\], a dominant theme is that use can be operationalized as a behavior or activity \[@burton-jones2007; \@mishra2017\]. In accordance, previous research suggests that observable behavior is a reliable measure of engagement and that other aspects, such as perception and intention, are directly related to it \[@dvir2018c; \@gill2015\]..

IE is the result of human-information interaction (HII), communication between the user and the information made available by the system \[@shneiderman2016a\], Although adoption and use are central constructs in IS, most research focuses on *technology use* rather than *information use*, which relates to the interaction between the user and the information itself independently of the system \[@wilson1981\]. Information Behavior Theory argues that the adoption and use of information are different than the adoption and use of IS \[@wilson1981\]. While research has been primarily concerned with a user's employment of a system, very little has examined the user's task-oriented behavior \[@wilson1981\]. Information behavior research seeks to understand how users search for and use information in various contexts, which transcends their use of technology \[@wilson1981\].

Wilson\'s model of information behavior outlines the following key factors relating to the user, the information system, and the information resource \[@wilson2010; \@wilson2000; \@wilson1997; \@wilson1981\].

-   **Information needs:** Physiological, cognitive, and affective demands that reflect personal factors, role demands, and environmental context. They define why the individual decides to look for information, what purpose the information they find will serve, and how the information is used once it is retrieved.

-   **Information-seeking and information-searching:** Purposive and active seeking and searching of information to satisfy a goal or answer a query. They are the micro-level behaviors employed by the searcher in interacting with IS of all kinds. To satisfy these needs, the searcher makes demands upon a system by acting as an intermediary and then evaluates the information provided by the system to determine if it satisfies the searcher's needs \[@wilson2000; \@wilson1981\].

-   **Activating mechanisms:** Factors that prompt a decision to seek information \[@wilson1997\].

-   **Information use:** Adoption, retrieval, and retention of the results of a query

In terms of information qualities, the model emphasizes attributes that are **objective, performance-based, and utilitarian**, such as functionality and relevancy, which address information needs; findability and discoverability, which relate to information seeking and searching; and, most importantly, information usability, defined as the efficiency of locating information, satisfaction with the quality of the information, and effectiveness of the information to fulfill needs \[@nielsen2005\].

**Wilson's (1981) modal faces several limitations**

-   Little research has examined how the model can measured systematically, applied to system design, or translated into changes in policy or practice \[\[CSL STYLE ERROR: reference with no printed form.\]\].

-   Little research has examined the link between usability and IE despite knowledge that usability is essential to IE but that IE, although always desirable, is not essential to usability \[@obrien2008a\].

-   Researchers need to move from studying use as a unidimensional to a multidimensional construct with dimensions driven differently by expectations, intentions, and facilitating conditions (Venkatesh et al. \[@venkatesh2008\]. This is supported by current research identifying the problems that can arise when individuals with limited cognitive abilities encounter massive amounts of potentially relevant information \[@chen2009; \@eppler2004\].

-   Although understanding cognitive ability and needs may provide insight into information behavior, research into this relationship has not been thoroughly explored \[@wilson2010; \@wilson2000\].

**While both IBT and UET are necessary for constructing the conceptual model, neither alone is sufficient. The table below** **shows how each complements the other to provide a fulsome basis for the model.**

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                           Information Behavior Theory                                             User Engagement Theory
  ------------------------ ----------------------------------------------------------------------- ---------------------------------------------------------------------------------------
  Focus                    Task                                                                    User

  User                     Information needs                                                       Perceptions and experience

  Information attributes   Functionality and usability                                             Aesthetic appeal, perceived usability, reward, focused attention

  Process                  Information needs, seeking, searching, and use; activating mechanisms   Point of engagement, sustained engagement, disengagement, and potential re-engagement

  Outcome                  Retrieval, retention, adoption, and use of information                  Experience and evaluation
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : . Study population

## Theoretical underpinning

### Cumulative Prospect Theory

Cumulative Prospect Theory (CPT) was used as the theoretical framework for this study \[@kahneman1979; \@tversky1992; \@tversky1974; \@tversky1981\]. Originally developed in the field of behavioral economics, CPT addresses users' affective and behavioral information needs by focusing on information processing and the importance of information context. According to CPT, one of the greatest challenges in understanding human behavior and decision-making is that much occurs at ‎a subconscious level. Gaining understanding of embodied cognition thus offers a powerful and effective way to ‎better understand the hidden drivers behind human judgment and decision-making.

Considering users' abilities and limitations, such as cognitive load, when making choices and decisions under terms of risk and ‎uncertainty, CPT recognizes two phases in the choice process, *framing* and *valuation*. ‎In the ‎framing phase, decision-makers construct a representation of the acts, ‎contingencies, and ‎outcomes relevant to a decision, while in the valuation phase they ‎estimate the ‎value of each prospect and choose accordingly.‎ CPT argues that cognitive processes can be partitioned into two main strategies, traditionally called *intuition* and *reason*. These processes result in two distinct approaches for decision-making, one that is spontaneous, intuitive, effortless, and rapid and one that is deliberate, rule-governed, effortful, and slow, respectively. These processes work in two fundamentally different ways depending on the context \[@kahneman2002a\].

Intuitive judgment is influenced by *heuristics*, simple, efficient rules used to form judgments and make decisions. Described as ‎‎mental shortcuts that usually involve focusing on one aspect of a complex problem and ignoring ‎others, heuristics work well under most circumstances. Nevertheless, they can lead to systematic deviations ‎from logic, probability, or ‎rational choice theory, resulting in *cognitive biases*, unconscious, automatic influences on human ‎judgment and ‎decision-making that ‎reliably produce reasoning ‎errors‎ \[@tversky1974\]. Thus, users' intuitive judgments based on data of limited validity and processed according to heuristic rules may lead to common biases. Whereas Engagement Theory (ET) and User Behavior Theory (UBT) suggest users' decisions are driven by awareness and rationality, CPT suggests that rationality and awareness are often limited and influenced by external factors, therefore stressing the importance of context.

Table 9. Comparison of Information Behavior Theory, Engagement Theory, and Cumulative Prospect Theory

+------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
|                        | Information Behavior Theory                               | Engagement Theory                                                                                 | Cumulative Prospect Theory                                                                                      |
+========================+===========================================================+===================================================================================================+=================================================================================================================+
| Focus                  | Task                                                      | User                                                                                              | System and context                                                                                              |
+------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Users                  | Information needs                                         | Perceptions and experience                                                                        | Heuristics and cognitive bias                                                                                   |
+------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Information attributes | Functionality and usability                               | Aesthetic appeal,                                                                                 | Framing and reference point (representation),                                                                   |
|                        |                                                           |                                                                                                   |                                                                                                                 |
|                        |                                                           | perceived usability, reward, and                                                                  | familiarity and informativeness (levels of uncertainty and risk reduction), and fluency (complexity and effort) |
|                        |                                                           |                                                                                                   |                                                                                                                 |
|                        |                                                           | focused attention                                                                                 |                                                                                                                 |
+------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Process                | Information needs, activating mechanisms,                 | Point of engagement, a period of sustained engagement, disengagement, and potential re-engagement | Framing and valuation                                                                                           |
|                        |                                                           |                                                                                                   |                                                                                                                 |
|                        | information seeking and searching, information use        |                                                                                                   |                                                                                                                 |
+------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
| Outcome                | Retrieval and retention of information (adoption and use) | Experience and evaluation                                                                         | Awareness, determination, and decision-making                                                                   |
+------------------------+-----------------------------------------------------------+---------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

: . Descriptive Statistics of Observations

## Literature review

Current research has been focused on *identifying* and *evaluating* IE but not *creating* IE \[@obrien2017; \@obrien2016d\]. While designing for IE has been an oft-cited goal of interactive system development in many disciplines, few guidelines have been developed for system designers to do so \[@blythe2005; \@overbeeke2003\]. In contrast, examination of the effect of information quality has been receiving greater attention, as research has shown that most decisions are now determined based on the digital information itself \[@lagun2016; \@lindgaard2006\]. Therefore, investigation of *information design* has become critical in the study of IE.

Information design is the quality of the information expression produced by the system's user interface (UI), defined as the components of an interactive system (software and hardware) that provide information for users to accomplish specific tasks \[@iso92412019\]. This study hypothesizes that the way information is delivered by the UI plays a large role in how and when it is used, engaged with, and experienced. For example, by providing what is colloquially known as "digital nudging," the employment of UI design elements can guide user (e.g., consumer) behavior and manipulate user (e.g., consumer) choices \[@weinmann2016\].

Several studies investigating information attributes have used textual analysis and computational linguistics tasks relating to IE to predict the memorability of movie quotes \[@cheng2012\] or the comedic value of cartoon captions \[@shahaf2015\]. In relation to specific words, computational linguistics has been used to predict word popularity or frequency \[@turney2019\]. These factors---memorability, entertainment value, and frequency of words and phrases---are aspects of IE.

There have been increasing calls for emphasizing *context* and *contextual theorizing* for IS research (Hong et al., 2013; Te'eni, 2015; Te'eni, 2016). While context can be defined as "situational opportunities and constraints that affect the occurrence and meaning behavior as well as functional relationships between variables" (Johns, 2006, p. 386), there is no agreement on which contextual factors affect IE and how to design for it.

How users interact with and disseminate information is a well-studied process in the IE literature. Defined as a \"cognitive commitment" (Mollen & Wilson, 2010) and "a psychological investment" (Bomia et al., 1997), *user engagement* is described as an immersive and captivating experience (Csikszentmihalyi, 1997). The works of Heath (2007), Berger (2013), Seiter (2014), and others have shed light on how information "flow" is impacted by cognitive‎ and emotional triggers, such as positive and negative signaling, information ‎asymmetry, processing fluency, and the link between familiarity and perception. 

There have been recent advancements in computational approaches to studying engagement. Among them, Berger and Milkman (2009) performed semi-automated sentiment analysis to quantify the affectivity and emotionality of *New York Times* articles, while Guerini et al. (2011) employed NLP techniques to explore text virality in social networks. In a manner similar to the proposed method in this study, Cheng, Kleinberg, and Lee (2012) developed algorithms for evaluating movie quotes by exploring patterns of influence and memorability. Based on their finding, they concluded that simple syntax, generality, ‎and ‎‎distinctiveness are important attributes of engagement.

To the best of my knowledge, no study has yet examined the relationship between content strategy and engagement. Most of the related research has focused on investigating *how* users react to information rather than *why* users become engaged with content. Also understudied and warranting investigation is *how* to develop engaging content rather than simply measuring it. The expected findings of this study may assist in the development of a new systematic approach to optimizing engagement, which includes lexical substitution in a given text.

### Theoretical Underpinning 

#### Framing Effect {#framing-effect .unnumbered}

Cumulative Prospect Theory (CPT), which was introduced in [Section 3.3.1](#cumulative-prospect-theory), served as the theoretical framework for this study. The main tenets of CPT are that people tend ‎to think of possible outcomes relative to a certain reference point rather than to a specific outcome, a phenomenon called the *framing ‎effect*.‎ The framing of problems adopted by decision-makers results from both extrinsic manipulation ‎‎of the options offered (i.e., the context) and of forces intrinsic to decision-makers (i.e., cognitive ability).

## Conceptual Framework for Digital Information Engagement with Text

This section presents the theoretically derived framework that guided this study. The purpose of this conceptual framework was to condense the mapping and explain the main themes of interest (e.g., key factors, variables, and constructs) and the presupposed boundaries or relationships among them \[@miles2014\]. The development of a conceptual framework followed an approach suggested by Webster and Watson \[@webster2002\]. After the various contributions to research were analyzed and compared, an inductive method of generalization was used to abstract common properties and formulate general concepts from specific instances. By synthesizing theoretical frameworks and domain literature, this part of theory development aimed to address the three research questions.

As previously described, IE is defined as the quality of information behavior and manifested in affective, behavioral, and cognitive investment and involvement when the user interacts with information. For successful communication, information must be transmitted through interaction, translated through interpretation, and ultimately transformed into knowledge through integration. **This process can be seen and measured using the three IE dimensions that were recognized through the literature review and the theoretical synthesis of IBT and UET.**

The first dimension is ***Perception**,* which can be described as a mental impression, a way of regarding, understanding, or interpreting a phenomenon \[@2021\]. More specifically, it refers to the users' experience with, attitude toward, relation to, emotional involvement with, interest in, and intention for the information. As suggested earlier, it can be measured using the UES, a series of evaluation questions \[@obrien2018\]. Measurement of **perception** is necessary but not sufficient to measure engagement; This leads to the second dimension of IE, which is **participation.** According to UET, behaviors, specifically the point of engagement, must also be measured. According to IBT, **participation** is a form of **information use** which is driven by the information itself and can be measured by information exchange, whether passive (information retrieval) or active (user reactions).

In this study, information will be represented, expressed, and communicated using words. Participation and perception will be measured through responses to the information, specifically selection and evaluation of words. In accordance, Hypothesis 1 proposes that participation in information interactions will also result in higher perception rates.

### H~1~: Selected words will have significantly higher user engagement (evaluation) {#h1-selected-words-will-have-significantly-higher-user-engagement-evaluation .unnumbered}

Null hypothesis (H0): µ ~evaluation/selected~ = µ ~evaluation/not\ selected~

Alternative hypothesis (Ha): µ ~evaluation/selected~ ≠ µ ~evaluation/not\ selected~

The process model of UE includes phases of sustained engagement and re-engagement \[@obrien2008a\]. These phases relate to the third dimension of IE which is *perseverance -* a cognitive response reflecting the level of information integration and influence. According to IBT, it can be seen as the quality of information use which reflects information interpretation and integration. Perseverance can manifest through information retention and recollection, knowledge acquisition and diffusion, and even decision-making. It can be measured by examining information acquisition, retention, recall, decision-making, and employment.

This study suggests a positive relation between **[perception]{.underline}**, the interpretation and evaluation of information, and perseverance, seen in the integration and employment of information. In accordance, Hypothesis 2 proposes the following:

### H~2~: Remembered words will have significantly higher user engagement (evaluation) {#h2-remembered-words-will-have-significantly-higher-user-engagement-evaluation .unnumbered}

Null hypothesis (H0): µ ~evaluation/retained~ = µ ~evaluation/not\ retained~

Alternative hypothesis (Ha): µ ~evaluation/retained~ ≠ µ ~evaluation/not\ retained~ []{dir="rtl"}

According to IBT, user interactions with information differs from user interactions with technology; whereas the type of information platform (desktop, mobile, etc.) does not significantly affect the perception of the information that is read using it, the words used to present the information (i.e., word choice) significantly affects perception. Therefore, the wording of the information *in itself* affects perception.

It can be hypothesized that IE is influenced by *how* the information is expressed by the system's user interface and is *independent of* and not significantly impacted by technology, task, or user variables. **Hence, variations in the expression of information will lead to significantly different IE scores, resulting in different rates of selection, evaluation, and retention.**

In accordance, Hypothesis 3 proposes the following:

### H~3~: Different words will have variations in IE, measured by significant difference in participation (selection), perception (evaluation), and perseverance (retention) {#h3-different-words-will-have-variations-in-ie-measured-by-significant-difference-in-participation-selection-perception-evaluation-and-perseverance-retention .unnumbered}

a.  Null hypothesis (H0): µ = µ

Alternative hypothesis (Ha):): µ ≠ µ

b.  **Add**

As IBT and UET suggest positive relationship among perception, participation and perseverance (selection, evaluation, and retention), Hypothesis 4 proposes the following:

### H~4~: Words' IE scores (selection, evaluation, and retention rates) are positively correlated  {#h4-words-ie-scores-selection-evaluation-and-retention-rates-are-positively-correlated .unnumbered}

a.  Null hypothesis (H~0~):

Word selection and evaluation are positively correlated:

m ~selection~ = m ~evaluation~

alternative hypothesis (H~1~)

m ~selection~ ≠ m ~evaluation~

b.  Null hypothesis (H~0~):

Word retention and evaluation are positively correlated:

m ~retention~ = m ~evaluation~

alternative hypothesis (H~1~)

m ~retention~ ≠ m ~evaluation~

Lastly, information was defined as the meaning of data. Therefore, words with the same meaning, i.e. synonyms, will have the same information engagement. Therefore, participation, perception and perseverance levels will not significantly differ between words with the same meaning.

### H~5~: Synonymous words will not have significant difference between IE levels (participation, perception and perseverance)  {#h5-synonymous-words-will-not-have-significant-difference-between-ie-levels-participation-perception-and-perseverance .unnumbered}

The figure below shows the conceptual model of the study.

## Conceptual framework 

### Identifying textual predictors 

A comprehensive literature review of behavioral economics research, particularly Cumulative Prospect Theory (CPT) \[@kahneman1979; \@tversky1992; \@tversky1974; \@tversky1981\], revealed the four predictive dimensions of engaging words: *representativeness, ease-of-use, affect,* and *distribution*, referred henceforth as READ. These predictive dimensions, also called *attributes,* are derived from heuristics that have been empirically validated as simple means of predicting decision-making \[@czerlinski1999; \@gigerenzer1999\]. These heuristics can be mapped onto information attributes that are *situational, stable,* and *controllable* based on the important dimensions of Attribution Theory, which explains how individuals collect data to arrive at causal judgments \[@kelley1967\].

The following sections describe each predictor and its suggested operationalization.

#### Representativeness  {#representativeness .unnumbered}

When judging the representativeness of a new stimulus or event, individuals typically evaluate the degree of similarity between the stimulus or event and a certain standard or process \[@kahneman1972\]. In accordance, the *representativeness heuristic* is the tendency to assess the similarity of objects and organize them based on their association, allowing for increased functionality, familiarity, findability, and fluency. Based on the work of Kahneman and Tversky, representativeness attributes or predictors can be described as the group of meanings and associations associated with a piece of information. A word is a basic unit for the expression of meaning, but the mapping between words and meanings is many-to-many; a word may have one meaning (synonymy) or many meanings (polysemy). Generally, individuals prefer one word when selecting from a set of synonyms and prefer one meaning of a polysemous word over others to convey a meaning. This means that although a word can have several interpretations, is likely to be the most representative.

The representativeness attribute can be operationalized using semantic relation analysis, which evaluates equivalency, hierarchy, and association, as is described in the Methods section.

#### Ease-of-use  {#ease-of-use .unnumbered}

Ease-of-use in terms of textual information asserts that users prefer texts they find highly readable based on the level of their processing (cognitive/perceptual) fluency. Both perceptual fluency and readability have been shown to be stimuli and determinants of decision-making, perception, and memory \[@alter2008; \@tversky1974\]. Accessibility, the ease of processing information, has been specifically shown to influence engagement \[@dvir2018c\]. The *ease-of-processing heuristic* is a fundamental heuristic in metacognition that guides, and biases judgments about memory. Various studies have shown that information that is easy to process is judged to have been learned well, providing evidence of the fundamental importance of the ease-of-processing heuristic \[@kornell2011\].

*Language fluency* is one of a variety of terms used to characterize or measure language ability, often in conjunction with accuracy and complexity. Although there are no widely agreed-upon definitions or measures of language fluency, individuals are generally considered fluent if their use of language appears fluid, coherent, and paced appropriately. This relates to the *availability heuristic,* a mental shortcut that helps individuals understand the world by using information that they find easy to recall.

Calculating the complexity of a phrase in terms of word length (number of characters) and syllable number is one means of operationalizing and quantifying ease-of-processing heuristic. Another is its readability, of which several means of calculation exist, including the Flesch-Kincaid test.

#### Affect  {#affect .unnumbered}

In addition to its *denotational* or literal meaning, the emotional *connotation* or association that a word or phrase carries is critical in IE. An emotional connotation is frequently described as either positive or negative regarding its pleasing or displeasing emotional connection. *Valence* or hedonic tone is an affective quality referring to the intrinsic attractiveness or \"goodness" (positive valence) or the averseness or \"badness" (negative valence) of an individual, event, object, or situation \[@finucane2000\]. There is now compelling evidence that every stimulus evokes an affective evaluation that may occur subconsciously \[@kahneman2002a\]. The original *affect heuristic* explains why individuals often rely on their emotions rather than concrete information when making decisions. While using it allows them to reach a conclusion quickly and easily, doing so can also distort their thinking and lead them to make suboptimal choices.

*Affective valence* has been shown to influence decision-making and ultimately engagement \[@batra1986; \@commuri2008; \@finucane2000\]. Based on the original affect heuristic, which has been widely accepted as a major general-purpose heuristic, the affect attribute proposes that the level of a word's sentiment will have a significant impact on its level of engagement. *Emotional valence* can be operationalized by performing sentiment analysis, which aims at measuring, understanding, and quantifying the sentiment behind a text, e.g., whether it is positive, negative, or neutral, using NLP, computational linguistics, and text analysis \[@liu2012\].

#### Distribution  {#distribution .unnumbered}

The *distribution attribute* states that a term's frequency or level of dispersion or distinctiveness influences its familiarity and fluency, which in turn impacts its representativeness. The frequency of a word is positively correlated with its familiarity, which is also an indicator of its cultural association and readability. This correlation is related to the *recognition heuristic*, which posits that if one of two objects is recognized and the other is not, the recognized object is likely to have greater value with respect to a criterion. Having been used as a model in the psychology of judgment and decision-making \[@tversky1992\], the recognition heuristic relates to the *availability heuristic*, which assists individuals in understanding the world by using information easy to recall. For example, when comparing familiar and unfamiliar phrases, users have little recourse but to base their judgments on ease of retrieval or recognition \[@kahneman2002a\]. In a series of experiments, participants were shown to rely on feelings of familiarity when comparing uncertain quantities, such as the relative size of two cities \[@gigerenzer1996\]. This finding provides evidence that inferences are made based on functionality and familiarity, as users tend to prefer alternatives that are more recognizable and relevant.

Word frequency is an important factor in computational linguistics and NLP. Research has found that very frequent words are read and understood quickly and easily \[@brysbaert2011; \@savin1963\], with highly frequent words perceived and interpreted correctly and more easily than infrequent words \[@savin1963\]. In a study of the words used in the Internet Movie Database (IMDB), word frequency was shown to impact IE directly; specifically, high-frequency words were found to have a positive impact on IE \[@dvir2018f; \@dvir2019d\]. The *distribution attribute* can be operationalized using TDM to measure situational significance (saliency or scarcity). This attribute can be defined therefore in terms of scarcity -- the less scarce a word is, the higher its distribution.

### Developing a predictive model

The predictive model used in this study was developed by combining the textual attributes of the information described in the previous sections, specifically its functionality, feeling, fluency, familiarity, and findability. The model provides the means to systematically and quantitatively measure four IE attributes using textual analysis and computational linguistics. These IE attributes are *representativeness,* which relates to a word's perceived usability and reward, i.e., how usable and relevant a word is; *ease-of-use*, which relates to a word's cognitive load, i.e., its ability to be understood and promote focused attention; *affect,* which relates to a word's sensory appeal, i.e., how much the word stimulates the senses; and *distribution*, which relates to a word's perceived usability, i.e., its recognizability and relevance. Figure 1 summarizes the predictive textual measures of the READ model and Table 3 shows the four heuristics of wording and phrasing.

Table 10. Heuristics of Wording and Phrasing

  -----------------------------------------------------------------------------------------------------------------------------------------------------
  ATTRiBUTE            Definition                                                               Factor                     Measurement
  -------------------- ------------------------------------------------------------------------ -------------------------- ----------------------------
  representativeness   Number of associations and meanings formed with a word                   Familiarity                Semantic relation

  Ease-of-use          Level of complexity of and amount of cognitive load required by a word   Fluency (ability)          Simplicity

  Affect               Level of affect stimulated by a word                                     Feeling (attitude)         Sentiment analysis

                                                                                                                           

                                                                                                                           

  Distribution         Availability and recognizability of a word                               Frequency (availability)   Saliency/significance
  -----------------------------------------------------------------------------------------------------------------------------------------------------

  : . Correlations between IE levels

Combination of the four attributes, the ***R**epresentativeness, **E**ase-of-use, **A**ffect, and **D**istribution* attributes, yielded the ***READ** Model*, a means of systematic determination of the probability that a word will be engaging. In accordance with the model, the following hypotheses were developed:

#### H~1~: Words' representativeness, ease-of-use, affect, and distribution scores will predict their {#h1-words-representativeness-ease-of-use-affect-and-distribution-scores-will-predict-their .unnumbered}

**level of engagement**

#### H~2~: When there is more than one possible word to describe the same information, a word's representativeness, ease-of-use, affect. and distribution scores will predict whether a synonym is more engaging  {#h2-when-there-is-more-than-one-possible-word-to-describe-the-same-information-a-words-representativeness-ease-of-use-affect.-and-distribution-scores-will-predict-whether-a-synonym-is-more-engaging .unnumbered}

## Conceptual Framework

The findings from the earlier phases of this study were applied to construct a user-centered, information-based, and data-driven predictive approach and the READ Model to systematically assess and manipulate IE as shown in Figures 1 and 2, respectively.

![Alt text](./assets/media/image2.jpeg){width="6.229166666666667in" height="7.616753062117235in"}

Figure 7. Predictive approach to assessing and manipulating IE

![A black background with a blue arrow pointing to a black background Description automatically generated](./assets/media/image3.png){width="6.167361111111111in" height="2.7090277777777776in"}

Figure 8. The READ Model

Using TDM, computational linguistics, and NLP, the process and model were used to examine whether engaging words or terms could be systematically assessed using four predictors. The data collected was used to test the hypothesis that words and phrases can influence the level of participation, perception, and perseverance, the primary attributes of IE, when strategically placed in a given context. Confirmation of the hypothesis would provide support that IE can be systematically manipulated by substituting a word with a more engaging synonym without changing the overall meaning. It would, for example, help determine whether changing the word "maven" in the title "Is the Pirate Party the new *maven* of media accountability or a blended, self-serving movement?"[^2] to the word "star" so that the title becomes "Is the Pirate Party the new *star* of media accountability or a blended, self-serving movement?" would increase IE. Hypothesis 1 formally states this possibility.

### *H~1~: Use of more engaging words ("sticky words") will positively influence the level of IE with the entire text as measured by participation, perception, and perseverance.* {#h1-use-of-more-engaging-words-sticky-words-will-positively-influence-the-level-of-ie-with-the-entire-text-as-measured-by-participation-perception-and-perseverance. .unnumbered}

Modified sentences will have higher IE levels

# Study 1

### Study design

This study examined the relationship between the dimensions of IE and textual information. It focuses on how IE dimensions (participation, perception, and perseverance) are impacted by variation in phrasing, or how wording (the independent variable) impacts IE (the dependent variable).

Data were collected using large scale online user surveys administered through the Qualtric.com platform, and then analyzed using the statistical software SPSS, Stata, and Minitab.

### Compiling the Dataset

For the survey, 100 different words were chosen randomly from WordNet \[@princetonuniversityWordNet2018\][^3]. WordNet is a large lexical database of English phrases grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept or meaning \[@miller1995\]. The dataset was compiled by randomly selecting sets of synonymous words representing 50 synsets. For example, the words "star" and "maven" belong to the same synset because they share a meaning in WordNet ("someone who is dazzlingly skilled in any field"). For the complete list of words, see Table below and [Section 5.4](#_Word_pairs).

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **Word1**             **Word2**          **Synset**             **Definition**
  --------------------- ------------------ ---------------------- ------------------------------------------------------------------------------------------------------------------------------------------------------------------
  **abused**            **maltreated**     abused.a.02            subjected to cruel treatment

  **star**              **maven**          ace.n.03               someone who is dazzlingly skilled in any field

  **quick**             **nimble**         agile.s.01             moving quickly and lightly

  **rich**              **plenteous**      ample.s.02             affording an abundant supply

  **annoying**          **nettlesome**     annoying.s.01          causing irritation or annoyance

  **art**               **prowess**        art.n.03               a superior skill learned by study, practice, and observation

  **gone**              **deceased**       asleep.s.03            dead

  **zombie**            **automaton**      automaton.n.01         someone who acts or responds in a mechanical or apathetic way

  **greedy**            **avaricious**     avaricious.s.01        immoderately desirous of acquiring something, typically wealth

  **king**              **magnate**        baron.n.03             a very wealthy or powerful businessman

  **mother**            **engender**       beget.v.01             make children

  **bubbling**          **belching**       burp.v.01              expel gas from the stomach

  **fighter**           **belligerent**    combatant.n.01         someone who fights or is fighting

  **computerization**   **cybernation**    computerization.n.01   the control of processes by computer

  **cut**               **shortened**      cut.s.03               with parts removed

  **lady**              **gentlewoman**    dame.n.02              a woman of refinement

  **death**             **demise**         death.n.04             the time at which life begins to end and continuing until death

  **going**             **departure**      departure.n.01         the act of departing

  **surrogate**         **deputy**         deputy.n.04            a person appointed to represent or act on behalf of others

  **find**              **uncovering**     discovery.n.01         the act of discovering something

  **dove**              **peacenik**       dove.n.02              someone who prefers negotiations to armed conflict in the conduct of foreign relations

  **done**              **coif**           dress.v.16             to arrange attractively

  **enemy**             **opposition**     enemy.n.02             an armed adversary, especially a member of an opposing military force

  **foodie**            **epicurean**      epicure.n.01           a person devoted to refined, sensuous enjoyments, especially good food and drink

  **exile**             **deportee**       exile.n.02             a person who is expelled from a home or country by authority

  **lush**              **profuse**        exuberant.s.03         produced or growing in extreme abundance

  **sticky**            **mucilaginous**   gluey.s.01             having the sticky properties of an adhesive

  **hit**               **smasher**        hit.n.03               a conspicuous success

  **ill**               **poorly**         ill.r.01               in a poor or improper or unsatisfactory manner; not well

  **now**               **forthwith**      immediately.r.01       without delay or hesitation; with no time intervening

  **reciprocation**     **interchange**    interchange.n.02       mutual interaction; the activity of reciprocating or exchanging, especially information

  **natural**           **lifelike**       lifelike.s.02          free from artificiality

  **just**              **merely**         merely.r.01            and nothing more

  **motive**            **need**           motivation.n.01        the psychological feature that arouses an organism to action toward a desired goal; the reason for the action that which gives purpose and direction to behavior

  **being**             **organism**       organism.n.01          a living thing that has or can develop the ability to act or function independently

  **pale**              **blanch**         pale.v.01              turn pale, as if in fear

  **puff**              **gasp**           pant.v.01              breathe noisily, as when one is exhausted

  **soul**              **mortal**         person.n.01            a human being

  **pirate**            **buccaneer**      pirate.n.02            someone who robs at sea or plunders the land from the sea without having a commission from any sovereign nation

  **dress**             **primp**          preen.v.03             dress or groom with elaborate care

  **rot**               **putrefaction**   putrefaction.n.01      a state of decay usually accompanied by an offensive odor

  **real**              **tangible**       real.s.04              capable of being treated as fact

  **sex**               **gender**         sex.n.04               the properties that distinguish organisms on the basis of their reproductive roles

  **termination**       **ending**         termination.n.05       the act of ending something

  **right**             **veracious**      veracious.s.02         precisely accurate

  **wash**              **lave**           wash.v.02              cleanse one\'s body with soap and water

  **best**              **easily**         well.r.03              indicating high probability; in all likelihood

  **better**            **well**           well.r.11              in a manner affording benefit or advantage

  **witch**             **wiccan**         wiccan.n.01            a believer in Wicca
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : . Descriptive Statistics of Words Analyzed

### Participants 

**[Recruitment:]{.underline}** Participants were recruited via a listserv sent to undergraduate students at a large research university in the United States. After completing the online survey, the participants were asked to forward invitations to their acquaintances, i.e., snowball sampling.

Prior to recruitment, the recruitment method and use of a survey study had been reviewed and approved by the University at Albany Institutional Review Board (IRB Study No. 22X113) and all participants had provided informed consent.

The system verified that the survey was only completed once, therefore controlling for unique participants. Overall, 80,500 observations were collected from 8,561 distinct participants. The mean number of words evaluated by a single participant was 9.446139.

**[Selection criteria:]{.underline}** Only undergraduate students completed the survey.

**[Characteristics:]{.underline}** All of the observations were by undergraduate students who voluntarily agreed to complete the survey and signed an informed consent form. The table below summarizes the composition of the study population.

+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                |                                                                       | > Count   | > N %       |
+================+=======================================================================+===========+=============+
| > Ethnicity    | > Asian                                                               | > 26780   | > 33.3%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > White                                                               | > 24043   | > 29.9%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Black or African American                                           | > 23497   | > 29.2%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Latin                                                               | > 5759    | > 7.2%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Native Hawaiian or Pacific Islander                                 | > 421     | > 0.5%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > AgeGroup     | > 17-22                                                               | > 60584   | > 75.3%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > 23-29                                                               | > 19508   | > 24.2%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > 30 and above                                                        | > 408     | > 0.5%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > Gender       | > male                                                                | > 47317   | > 58.8%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > female                                                              | > 33183   | > 41.2%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > AcademicYear | > Senior                                                              | > 33811   | > 42.0%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Junior                                                              | > 25179   | > 31.3%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > sophomore                                                           | > 11123   | > 13.8%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Freshman                                                            | > 10387   | > 12.9%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > EngLevel     | > native speaker                                                      | > 63267   | > 78.6%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > excellent command / highly proficient in spoken and written English | > 6143    | > 7.6%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > near native / fluent                                                | > 4865    | > 6.0%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > good command / good working knowledge                               | > 2605    | > 3.2%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > basic communication skills / working knowledge                      | > 1856    | > 2.3%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > very good command                                                   | > 1764    | > 2.2%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > Major        | > Accounting and Law                                                  | > 10465   | > 13.0%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Marketing                                                           | > 9167    | > 11.4%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Finance                                                             | > 7652    | > 9.5%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Management                                                          | > 6344    | > 7.9%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Economics                                                           | > 5940    | > 7.4%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Mathematics and Statistics                                          | > 3211    | > 4.0%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Psychology                                                          | > 2839    | > 3.5%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Information Science                                                 | > 2820    | > 3.5%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Criminal Justice                                                    | > 2735    | > 3.4%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Communication                                                       | > 2668    | > 3.3%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > English                                                             | > 2664    | > 3.3%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Computer Science                                                    | > 2635    | > 3.3%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Philosophy                                                          | > 2545    | > 3.2%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Political Science                                                   | > 2529    | > 3.1%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Physics                                                             | > 2513    | > 3.1%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Sociology                                                           | > 2462    | > 3.1%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Africana Studies                                                    | > 2400    | > 3.0%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Anthropology                                                        | > 2276    | > 2.8%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Environmental and Sustainable Engineering                           | > 2252    | > 2.8%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Biomedical Sciences                                                 | > 2224    | > 2.8%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > History                                                             | > 2159    | > 2.7%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > device       | > laptop                                                              | > 56447   | > 70.1%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > mobile                                                              | > 12588   | > 15.6%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > desktop                                                             | > 11465   | > 14.2%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > OS           | > macOS                                                               | > 34354   | > 42.7%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Windows                                                             | > 32512   | > 40.4%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > iOS                                                                 | > 11842   | > 14.7%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Chrome OS                                                           | > 986     | > 1.2%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Android                                                             | > 806     | > 1.0%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
| > Browser      | > Chrome                                                              | > 45668   | > 56.7%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Safari                                                              | > 25523   | > 31.7%     |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Edge                                                                | > 6903    | > 8.6%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Firefox                                                             | > 2101    | > 2.6%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+
|                | > Opera                                                               | > 305     | > 0.4%      |
+----------------+-----------------------------------------------------------------------+-----------+-------------+

: . Descriptive Statistics for IE Dimensions

The table shows that the majority of the participants were seniors (33,811 responses, 42%). The mean age was 22.1 (SD = 1.388), with 75.3% of responses belonging to the age group of 17-22. 41.2% of the responses were by females and 58.8% by males. More than 95.0% reported that their English proficiency was at least "very good," with 79.0% identifying as native speakers.

The most popular major was Accounting and Law (10,465 responses, 13%), following by Marketing (12.0%) and Finance (9.4%). Regarding race and ethnicity, 37.6% identified as Asian, 31.6% as Black or African American, 24.9% as White, and 5.7% as Latinx.

Using Qualtrics, metadata were collected on the technology used by the participants to complete the surveys. The majority of the observations were submitted through a laptop device (70.1%), followed by mobile devices (15.6%) and desktops (14.2%). This may be attributed to the survey being easier to read and complete on a large screen, as was reported by participants in early stages of the survey design. The most popular operating systems were MacOS on laptop devices (40.8%), Windows on desktops (40.4%) and iOS on mobile. The most popular browser was Google Chrome (56.7%) followed by Safari (31.7%).

**Sampling and randomization**

Each participant was presented 7--10 words from the dataset in random order, with great importance placed on the randomization and control variables. Each word of the dataset was presented exactly 805 times, using randomization to control for the display order (DO) and the participants' characteristics. By balancing both known and unknown predictive factors, the survey design aimed to reduce biases, such as selection bias and allocation bias, to the greatest extent possible.

Chi-square analysis of the goodness of fit of the samples revealed that the characteristic composition for each word sample was comparable to that of the overall population. Pearson chi-square analysis between demographic groups and between word samples revealed no significant differences for all χ2 (Φ = 1).

  -----------------------------------------------------------------------

  -----------------------------------------------------------------------

  : . Regression Results of UES Prediction Based on READ Features

### Measures

After participants provided their informed consent ([see section 5.2](#_Introduction_and_informed)) and answered several demographic questions ([see section 5.3](#_Demographic_questions)), they completed the survey to measure their responses to textual information to assess their perception, participation, and perseverance, the three dimensions of IE

1.  **Perception**

Perception was measured as affective evaluation of the information. Participants were presented with a randomized list of words and asked to evaluate it based on statements adopted from the UES \[@obrien2018\]. Participants used an 8-item Likert scale to assess each word's sensory appeal, focused attention, perceived usability, and reward (for a list of statements used, see [section 5.5](#_Word_evaluation)). Statements were presented in random order, with 4 positively formulated (e.g., "This word appealed to my senses" or "this word is easy to understand") and 4 negatively formulated (e.g., "This word is not usable"). Participants indicated how much they agreed or disagreed with each statement using a 5-point scale ranging from strongly disagree (1) to strongly agree (5). The responses to the negative statements were reverse-coded to maintain a unified 8-item scale. Testing for scale reliability revealed a Cronbach's alpha of 0.888.

2.  **Participation**

Participation was measured as behavioral reactions and retrieval of the information. To measure participation, the participants were asked to click on the words with which they would like to engage. For each word, a selection response was recorded ("1" or "0"), and was used to calculate selection rates.

3.  **Perseverance**

Perseverance was measured as retention of the information in terms of memory. The participants were asked to write the words they remembered from the list previously presented. For each word, a retention measurement was recorded ("1" if remembered, "0" if not).

## Results

[Data for study 1 can be found in the following link.](https://drive.google.com/file/d/13LRh1-qOa3yR20QlL89RHjkZyujK_3Ov/view?usp=sharing)

### Hypothesis 1: Words that are selected will have significantly higher UES scores than words that are not selected {#hypothesis-1-words-that-are-selected-will-have-significantly-higher-ues-scores-than-words-that-are-not-selected .unnumbered}

+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
|                                                                                | > N       | > Mean  | > Std. Deviation | > Variance |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
| > Select                                                                       | > 80500   | > .218  | > .413           | > .171     |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
| > Retention                                                                    | > 80500   | > .081  | > .272           | > .074     |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
| > Mean UES score                                                               | > 80500   | > 2.437 | > .877           | > .770     |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
| > Evaluation rate                                                              | > 80500   | > .487  | > .175           | > .031     |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
| > Valid N (listwise)                                                           | > 80500   |         |                  |            |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+
| > Note. Standard deviation and variance use N rather than N-1 in denominators. |           |         |                  |            |
+--------------------------------------------------------------------------------+-----------+---------+------------------+------------+

: . Regression Results of Selection Prediction Based on READ Features

Participants selected 17,858 words out of 80,500 observations, leading to selection rate of μ = 21.8%. For all observations, the mean of the evaluations, calculated as the average UES, was μ = 2.43. For the selected words, the mean of the UES was 2.75870 , while the mean UES for unselected words was 2.34900. A t-test of independent means comparing evaluation scores of selected and unselected words across all observations revealed a significant effect size (t\[24613.834\] = 49.635, p = .0000, d=.862010). As hypothesized, selected words had significantly higher mean UES scores in comparison to the unselected words.

### Hypothesis 2: Words that are remembered will have significantly higher UES scores compared to words that are not remembered  {#hypothesis-2-words-that-are-remembered-will-have-significantly-higher-ues-scores-compared-to-words-that-are-not-remembered .unnumbered}

Out of observations, only 8.1% of words, or 6,616 were remembered. A t-test of independent means to assess the difference in evaluation scores between remembered and unremembered words revealed a significant effect size (t\[7410.500\] = 39.880, p = 0.0000, d = 0.866714. As hypothesized, remembered words had significantly higher mean UES scores, with a mean of 2.92 (or 58%) compared to a mean of 2.39 for unremembered words, thereby confirming Hypothesis 2.

+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
| > **Group Statistics** |             |             |               |                      |                       |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
|                        | > select    | > N         | > Mean        | > Std. Deviation     | > Std. Error Mean     |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
| > UES                  | > 0         | > **62944** | > **2.34744** | > **.812522**        | > **.003239**         |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
|                        | > 1         | > **17556** | > **2.75768** | > **1.015529**       | > **.007664\`**       |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
|                        | > retention | > N         | > **Mean**    | > **Std. Deviation** | > **Std. Error Mean** |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
| > UESavg               | > 0         | > 74006     | > **2.39455** | > **.848546**        | > **.003119**         |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+
|                        | > 1         | > 6494      | > **2.91970** | > **1.041039**       | > **.012918**         |
+------------------------+-------------+-------------+---------------+----------------------+-----------------------+

: . Regression Results of Retention Prediction based on READ Features

<table>
<caption><p>. Residual Statistics of UES prediction</p></caption>
<colgroup>
<col style="width: 5%" />
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="11"><blockquote>
<p><strong>Independent Samples Test</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2" rowspan="3">UES</td>
<td colspan="2"><blockquote>
<p>Levene's Test for Equality of Variances</p>
</blockquote></td>
<td colspan="7"><blockquote>
<p>t-test for Equality of Means</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>F</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Sig.</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>t</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>df</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Sig. (2-tailed)</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Mean Difference</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Std. Error Difference</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>95% Confidence Interval of the Difference</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Lower</p>
</blockquote></td>
<td><blockquote>
<p>Upper</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Selection</p>
</blockquote></td>
<td><blockquote>
<p>Equal variances assumed</p>
</blockquote></td>
<td><blockquote>
<p><strong>5144.461</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.000</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-55.832</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>80498</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.000</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.410241</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.007348</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.424642</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.395839</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Equal variances not assumed</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>-49.304</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>24168.606</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.000</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.410241</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.008321</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.426550</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.393932</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>Retention</p>
</blockquote></td>
<td><blockquote>
<p>Equal variances assumed</p>
</blockquote></td>
<td><blockquote>
<p>1840.388</p>
</blockquote></td>
<td><blockquote>
<p><strong>.000</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-46.873</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>80498</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.000</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.525149</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.011204</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.547108</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.503190</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Equal variances not assumed</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p><strong>-39.516</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>7269.973</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.000</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.525149</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>.013290</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.551201</strong></p>
</blockquote></td>
<td><blockquote>
<p><strong>-.499098</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

: . Residual Statistics of UES prediction

+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
| > **Independent Samples Effect Sizes** |                       |                   |                  |                           |             |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
| UESavg                                 |                       | > Standardizer^a^ | > Point Estimate | > 95% Confidence Interval |             |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
|                                        |                       |                   |                  | > Lower                   | > Upper     |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
| > Selection                            | > Cohen\'s d          | > **.860885**     | > **-.477**      | > **-.493**               | > **-.460** |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
|                                        | > Hedges\' correction | > **.860893**     | > **-.477**      | > **-.493**               | > **-.460** |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
|                                        | > Glass\'s delta      | > **1.015529**    | > **-.404**      | > **-.421**               | > **-.387** |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
| > Retention                            | > Cohen\'s d          | > **.865661**     | > **-.607**      | > **-.632**               | > **-.581** |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
|                                        | > Hedges\' correction | > **.865669**     | > **-.607**      | > **-.632**               | > **-.581** |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+
|                                        | > Glass\'s delta      | > **1.041039**    | > **-.504**      | > **-.531**               | > **-.478** |
+----------------------------------------+-----------------------+-------------------+------------------+---------------------------+-------------+

: . Residual Statistics of Selection rate

### Hypothesis 3: Different words will have variations in IE, measured by significant difference in participation (selection), perception (evaluation), and perseverance (retention) {#hypothesis-3-different-words-will-have-variations-in-ie-measured-by-significant-difference-in-participation-selection-perception-evaluation-and-perseverance-retention .unnumbered}

We calculated the IE scores for all 100 words in terms of probability to be selected, to be remembered and average perception. The complete table is in [section 6.1.1](#_IE_scores_for).

A one-way ANOVA was conducted to compare evaluation, selection, and retention rates between words. Results revealed significant differences between words in evaluation rate (F\[99\], 80400) = 48.579, p = .000, 𝜼𝟐=.056), selection rates (F\[99, 80400\] = 1.481, p = .001, 𝜼𝟐=.002), and retention rates (F\[99\], 80400) = 1.921, p = .001, 𝜼𝟐=.002).

+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              |                  | > SS        | > df    | > MS     | > F      | > Sig.   | > 𝜼𝟐   |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
| > Evaluation | > Between Groups | > 3497.624  | > 99    | > 35.330 | > 48.579 | > .000   | > .056 |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              | > Within Groups  | > 58471.551 | > 80400 | > .727   |          |          |        |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              | > Total          | > 61969.175 | > 80499 |          |          |          |        |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
| > Select     | > Between Groups | > 24.985    | > 99    | > .252   | > 1.481  | > .001   | > .002 |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              | > Within Groups  | > 13702.281 | > 80400 | > .170   |          |          |        |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              | > Total          | > 13727.265 | > 80499 |          |          |          |        |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
| > retention  | > Between Groups | > 14.087    | > 99    | > .142   | > 1.921  | > \<.001 | > .002 |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              | > Within Groups  | > 5956.037  | > 80400 | > .074   |          |          |        |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+
|              | > Total          | > 5970.124  | > 80499 |          |          |          |        |
+--------------+------------------+-------------+---------+----------+----------+----------+--------+

: . Residual Statistics of Retention Level

Single sample t-tests (X̄ ≠ µ) were used to compare each of the words IE level means (selection, evaluating, retention) and the general population means to test for significant difference. For perception, measured through mean of evaluation (UES), 76 words had M significantly different than the population mean: 30 words had average evaluation (ues) significantly greater than the population mean and 48 words had X̅~ues~ significantly smaller than the population mean (all t-values \> 1.8 or \<--1.8, p\<0.05).

For participation, measured through selection, 17 words had x̅ significantly different than the population mean. For perseverance, 18 words had x̅ retention rate significantly different than the population mean.

The results showed that specific words had significantly different (higher or lower) selection rates, retention rate, and UES scores. The Single sample t-tests confirmed that specific words are more or less engaging than others, regardless of users' demographics, display order or technology used. The tables below show example of words that were scored significantly higher in all IE scale midpoints.

Comparison of the word means on all three IE levels revealed that some words have significantly higher means on all three IE levels, some on only one or two, while others have significantly lower means on all three IE levels.

The graphs below show the difference between the words (I need to pick out one of them).

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  Word   *n*   X̄ues   SDues   *t*ues   p-value(ues)   α(ues)   SIGues   ∑select   X̄select   t(select)   p-value(select)   α(select)   SIGselect   ∑retention   X̄retention   t(retention)   p-value(retention)   α(retention)   SIGretention   IElevel
  ------ ----- ------ ------- -------- -------------- -------- -------- --------- --------- ----------- ----------------- ----------- ----------- ------------ ------------ -------------- -------------------- -------------- -------------- ---------

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

  : . Observed and Predicted UES Scores for 50 Synsets

### Hypothesis 4: Words' IE scores (selection, evaluation, and retention rates) are positively correlated - [Breakdown]{.mark} {#hypothesis-4-words-ie-scores-selection-evaluation-and-retention-rates-are-positively-correlated---breakdown .unnumbered}

A statistically significant positive correlation was found between a word's UES score and its selection rate, r(100) = .64, p \< .001. Words with higher UES also tended to have higher retention rates, r(100) = .63, p \< .001.

+--------------+-------------------------------------+--------------+--------+--------------+
|              |                                     | > Mselect    |        | > Mretention |
+--------------+-------------------------------------+--------------+--------+--------------+
| > MUES       | > Pearson Correlation               | > .636^\*\*^ | > 1    | > .625^\*\*^ |
+--------------+-------------------------------------+--------------+--------+--------------+
|              | > Sig. (2-tailed)                   | > \<.001     |        | > \<.001     |
+--------------+-------------------------------------+--------------+--------+--------------+
|              | > Sum of Squares and Cross-products | > .060       | > .293 | > .045       |
+--------------+-------------------------------------+--------------+--------+--------------+
|              | > Covariance                        | > .001       | > .003 | > .000       |
+--------------+-------------------------------------+--------------+--------+--------------+
|              | > N                                 | > 100        | > 100  | > 100        |
+--------------+-------------------------------------+--------------+--------+--------------+
|              |                                     |              |        |              |
+--------------+-------------------------------------+--------------+--------+--------------+

: . Observed and Predicted Selection Rate for 50 Synsets

![Chart, line chart Description automatically generated](./assets/media/image4.png){width="6.5in" height="4.5993055555555555in"}

We also ran linear regression predicting participation (selection rate) and perception (retention rate) from the perception score (mean UES for each word).

The standardized regression coefficients were .630 for selection and .631 for retention, both are statistically significant (t=8.03 and t= .631).

<table>
<caption><p>. Observed and Predicted Retention Rate for 50 Synsets</p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="14"><blockquote>
<p><em>Coefficients<sup>a</sup></em></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2" rowspan="2"><blockquote>
<p>Model</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Unstandardized Coefficients</p>
</blockquote></td>
<td><blockquote>
<p>Standardized Coefficients</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>t</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Sig.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>95.0% Confidence Interval for B</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Correlations</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Collinearity Statistics</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>Std. Error</p>
</blockquote></td>
<td><blockquote>
<p>Beta</p>
</blockquote></td>
<td><blockquote>
<p>Lower Bound</p>
</blockquote></td>
<td><blockquote>
<p>Upper Bound</p>
</blockquote></td>
<td><blockquote>
<p>Zero-order</p>
</blockquote></td>
<td><blockquote>
<p>Partial</p>
</blockquote></td>
<td><blockquote>
<p>Part</p>
</blockquote></td>
<td><blockquote>
<p>Tolerance</p>
</blockquote></td>
<td><blockquote>
<p>VIF</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>(Constant)</p>
</blockquote></td>
<td><blockquote>
<p>.088</p>
</blockquote></td>
<td><blockquote>
<p>.016</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>5.447</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>.056</p>
</blockquote></td>
<td><blockquote>
<p>.121</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mues</p>
</blockquote></td>
<td><blockquote>
<p>.053</p>
</blockquote></td>
<td><blockquote>
<p>.007</p>
</blockquote></td>
<td><blockquote>
<p>.630</p>
</blockquote></td>
<td><blockquote>
<p>8.030</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>.040</p>
</blockquote></td>
<td><blockquote>
<p>.066</p>
</blockquote></td>
<td><blockquote>
<p>.630</p>
</blockquote></td>
<td><blockquote>
<p>.630</p>
</blockquote></td>
<td><blockquote>
<p>.630</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="14"><blockquote>
<p>a. Dependent Variable: Mselect</p>
</blockquote></td>
</tr>
</tbody>
</table>

: . Observed and Predicted Retention Rate for 50 Synsets

<table>
<caption><p>. Titles Evaluated for IE</p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="14"><blockquote>
<p><em>Coefficients<sup>a</sup></em></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2" rowspan="2"><blockquote>
<p>Model</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Unstandardized Coefficients</p>
</blockquote></td>
<td><blockquote>
<p>Standardized Coefficients</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>t</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Sig.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>95.0% Confidence Interval for B</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Correlations</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Collinearity Statistics</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>Std. Error</p>
</blockquote></td>
<td><blockquote>
<p>Beta</p>
</blockquote></td>
<td><blockquote>
<p>Lower Bound</p>
</blockquote></td>
<td><blockquote>
<p>Upper Bound</p>
</blockquote></td>
<td><blockquote>
<p>Zero-order</p>
</blockquote></td>
<td><blockquote>
<p>Partial</p>
</blockquote></td>
<td><blockquote>
<p>Part</p>
</blockquote></td>
<td><blockquote>
<p>Tolerance</p>
</blockquote></td>
<td><blockquote>
<p>VIF</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>(Constant)</p>
</blockquote></td>
<td><blockquote>
<p>-.017</p>
</blockquote></td>
<td><blockquote>
<p>.012</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>-1.388</p>
</blockquote></td>
<td><blockquote>
<p>.168</p>
</blockquote></td>
<td><blockquote>
<p>-.041</p>
</blockquote></td>
<td><blockquote>
<p>.007</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Mues</p>
</blockquote></td>
<td><blockquote>
<p>.040</p>
</blockquote></td>
<td><blockquote>
<p>.005</p>
</blockquote></td>
<td><blockquote>
<p>.631</p>
</blockquote></td>
<td><blockquote>
<p>8.048</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>.030</p>
</blockquote></td>
<td><blockquote>
<p>.050</p>
</blockquote></td>
<td><blockquote>
<p>.631</p>
</blockquote></td>
<td><blockquote>
<p>.631</p>
</blockquote></td>
<td><blockquote>
<p>.631</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="14"><blockquote>
<p>a. Dependent Variable: Mreten</p>
</blockquote></td>
</tr>
</tbody>
</table>

: . Titles Evaluated for IE

Logistic regression?

<table>
<caption><p>. Number of Observations for Title Variations</p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="14"><blockquote>
<p><em>Coefficients<sup>a</sup></em></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2" rowspan="2"><blockquote>
<p>Model</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Unstandardized Coefficients</p>
</blockquote></td>
<td><blockquote>
<p>Standardized Coefficients</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>t</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Sig.</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>95.0% Confidence Interval for B</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>Correlations</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Collinearity Statistics</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>B</p>
</blockquote></td>
<td><blockquote>
<p>Std. Error</p>
</blockquote></td>
<td><blockquote>
<p>Beta</p>
</blockquote></td>
<td><blockquote>
<p>Lower Bound</p>
</blockquote></td>
<td><blockquote>
<p>Upper Bound</p>
</blockquote></td>
<td><blockquote>
<p>Zero-order</p>
</blockquote></td>
<td><blockquote>
<p>Partial</p>
</blockquote></td>
<td><blockquote>
<p>Part</p>
</blockquote></td>
<td><blockquote>
<p>Tolerance</p>
</blockquote></td>
<td><blockquote>
<p>VIF</p>
</blockquote></td>
</tr>
<tr class="even">
<td rowspan="2"><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>(Constant)</p>
</blockquote></td>
<td><blockquote>
<p>-.003</p>
</blockquote></td>
<td><blockquote>
<p>.004</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>-.799</p>
</blockquote></td>
<td><blockquote>
<p>.424</p>
</blockquote></td>
<td><blockquote>
<p>-.012</p>
</blockquote></td>
<td><blockquote>
<p>.005</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>UESavg</p>
</blockquote></td>
<td><blockquote>
<p>.091</p>
</blockquote></td>
<td><blockquote>
<p>.002</p>
</blockquote></td>
<td><blockquote>
<p>.193</p>
</blockquote></td>
<td><blockquote>
<p>55.832</p>
</blockquote></td>
<td><blockquote>
<p>.000</p>
</blockquote></td>
<td><blockquote>
<p>.088</p>
</blockquote></td>
<td><blockquote>
<p>.094</p>
</blockquote></td>
<td><blockquote>
<p>.193</p>
</blockquote></td>
<td><blockquote>
<p>.193</p>
</blockquote></td>
<td><blockquote>
<p>.193</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="14"><blockquote>
<p>a. Dependent Variable: select</p>
</blockquote></td>
</tr>
</tbody>
</table>

: . Number of Observations for Title Variations

Finally, we ran a t-test for independent means to check if selection and retention rates were significantly higher for words that had statistically significant higher perception (UES score).

The results indicated that words with significantly higher UES scores are more likely to have significantly higher selection and retention rates, t(38.898) = 4.441, p = \<.001.022, d = .368 for selection, and t(43.126) = 2.711, p = .005, d = .421 for retention.

+------------------------+----------+--------+--------+------------------+-------------------+
| > **Group Statistics** |          |        |        |                  |                   |
+------------------------+----------+--------+--------+------------------+-------------------+
|                        | > SigUES | > N    | > Mean | > Std. Deviation | > Std. Error Mean |
+------------------------+----------+--------+--------+------------------+-------------------+
| > SigSelection         | > \>= 1  | > 29   | > .31  | > .471           | > .087            |
+------------------------+----------+--------+--------+------------------+-------------------+
|                        | > \< 1   | > 71   | > -.11 | > .318           | > .038            |
+------------------------+----------+--------+--------+------------------+-------------------+
| > SigRetention         | > \>= 1  | > 29   | > .21  | > .491           | > .091            |
+------------------------+----------+--------+--------+------------------+-------------------+
|                        | > \< 1   | > 71   | > -.07 | > .390           | > .046            |
+------------------------+----------+--------+--------+------------------+-------------------+

: . Differences between IE Dimensions of Original and Modified Titles

<table style="width:100%;">
<caption><p>. Difference in UES scores between titles</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 6%" />
<col style="width: 6%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="12"><blockquote>
<p><strong>Independent Samples Test</strong></p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2" rowspan="3"></td>
<td colspan="2"><blockquote>
<p>Levene's Test for Equality of Variances</p>
</blockquote></td>
<td colspan="8"><blockquote>
<p>t-test for Equality of Means</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>F</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Sig.</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>t</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>df</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>Significance</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Mean Difference</p>
</blockquote></td>
<td rowspan="2"><blockquote>
<p>Std. Error Difference</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>95% Confidence Interval of the Difference</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>One-Sided p</p>
</blockquote></td>
<td><blockquote>
<p>Two-Sided p</p>
</blockquote></td>
<td><blockquote>
<p>Lower</p>
</blockquote></td>
<td><blockquote>
<p>Upper</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>SigSelection</p>
</blockquote></td>
<td><blockquote>
<p>Equal variances assumed</p>
</blockquote></td>
<td><blockquote>
<p>20.375</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>5.209</p>
</blockquote></td>
<td><blockquote>
<p>98</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>.423</p>
</blockquote></td>
<td><blockquote>
<p>.081</p>
</blockquote></td>
<td><blockquote>
<p>.262</p>
</blockquote></td>
<td><blockquote>
<p>.584</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Equal variances not assumed</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>4.441</p>
</blockquote></td>
<td><blockquote>
<p>38.898</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>&lt;.001</p>
</blockquote></td>
<td><blockquote>
<p>.423</p>
</blockquote></td>
<td><blockquote>
<p>.095</p>
</blockquote></td>
<td><blockquote>
<p>.230</p>
</blockquote></td>
<td><blockquote>
<p>.616</p>
</blockquote></td>
</tr>
<tr class="odd">
<td rowspan="2"><blockquote>
<p>SigRetention</p>
</blockquote></td>
<td><blockquote>
<p>Equal variances assumed</p>
</blockquote></td>
<td><blockquote>
<p>6.043</p>
</blockquote></td>
<td><blockquote>
<p>.016</p>
</blockquote></td>
<td><blockquote>
<p>2.986</p>
</blockquote></td>
<td><blockquote>
<p>98</p>
</blockquote></td>
<td><blockquote>
<p>.002</p>
</blockquote></td>
<td><blockquote>
<p>.004</p>
</blockquote></td>
<td><blockquote>
<p>.277</p>
</blockquote></td>
<td><blockquote>
<p>.093</p>
</blockquote></td>
<td><blockquote>
<p>.093</p>
</blockquote></td>
<td><blockquote>
<p>.462</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Equal variances not assumed</p>
</blockquote></td>
<td></td>
<td></td>
<td><blockquote>
<p>2.711</p>
</blockquote></td>
<td><blockquote>
<p>43.126</p>
</blockquote></td>
<td><blockquote>
<p>.005</p>
</blockquote></td>
<td><blockquote>
<p>.010</p>
</blockquote></td>
<td><blockquote>
<p>.277</p>
</blockquote></td>
<td><blockquote>
<p>.102</p>
</blockquote></td>
<td><blockquote>
<p>.071</p>
</blockquote></td>
<td><blockquote>
<p>.484</p>
</blockquote></td>
</tr>
</tbody>
</table>

: . Difference in UES scores between titles

Therefore, it is possible to reject the Null hypothesis (H0) and conclude that there is a difference in information engagement between word variations.

### Hypothesis 5: Synonyms will have similar IE levels  {#hypothesis-5-synonyms-will-have-similar-ie-levels .unnumbered}

To determine if selection, UES, and retention rates are impacted by word choice regardless of the meaning, pairwise comparisons for independent means (X̅1 ≠ X̅2) were conducted to evaluate difference between synonymous words for each of the 50 synsets. The results revealed that 43 of the 50 synsets had significantly different IE scores (P \< 0.05).

  ---------------------------------------------------------------------------------------
  **Synset**                      **F**        **Sig.**   **effect size (η2)**   
  ---------------------------- -- ------------ ---------- ---------------------- --------
  ace.n.03                        219.299      0.001      0.120                  

  agile.s.01                      48.445       0.001      0.029                  

  ample.s.02                      348.764      0.001      0.178                  

  annoying.s.01                   50.29        0.001      0.030                  

  art.n.03                        100.247      0.001      0.059                  

  automaton.n.01                  140.521      0.001      0.080                  

  avaricious.s.01                 44.819       0.001      0.027                  

  baron.n.03                      211.834      0.001      0.116                  

  beget.v.01                      146.013      0.001      0.083                  

  burp.v.01                       27.557       0.001      0.017                  

  combatant.n.01                  16.615       0.001      0.010                  

  cut.s.03                        43.082       0.001      0.026                  

  dame.n.02                       22.739       0.001      0.014                  

  death.n.04                      188.083      0.001      0.105                  

  departure.n.01                  11.895       0.001      0.007                  

  discovery.n.01                  30.915       0.001      0.019                  

  dove.n.02                       73.082       0.001      0.043                  

  dress.v.16                      69.665       0.001      0.042                  

  enemy.n.02                      16.286       0.001      0.010                  

  epicure.n.01                    122.391      0.001      0.071                  

  exile.n.02                      36.504       0.001      0.022                  

  exuberant.s.03                  40.626       0.001      0.025                  

  gluey.s.01                      28.991       0.001      0.018                  

  hit.n.03                        10.441       0.001      0.006                  

  ill.r.01                        18.478       0.001      0.011                  

  immediately.r.01                74.127       0.001      0.044                  

  lifelike.s.02                   52.03        0.001      0.031                  

  merely.r.01                     32.281       0.001      0.020                  

  pale.v.01                       36.649       0.001      0.022                  

  person.n.01                     28.537       0.001      0.017                  

  pirate.n.02                     11.311       0.001      0.007                  

  preen.v.03                      49.306       0.001      0.030                  

  putrefaction.n.01               25.041       0.001      0.015                  

  real.s.04                       35.588       0.001      0.022                  

  sex.n.04                        97.868       0.001      0.057                  

  veracious.s.02                  79.195       0.001      0.047                  

  wash.v.02                       48.27        0.001      0.029                  

  well.r.03                       30.598       0.001      0.019                  

  wiccan.n.01                     27.517       0.001      0.017                  

  abused.a.02                     4.614        0.032      0.003                  

  pant.v.01                       4.262        0.039      0.003                  

  witness.n.01                    4.28         0.039      0.003                  

  interchange.n.02                4.023        0.045      0.002                  

  organism.n.01                   1.641        0.2        0.001                  

  computerization.n.01            1.156        0.282      0.001                  

  asleep.s.03                     0.537        0.464      0.000                  

  motivation.n.01                 0.513        0.474      0.000                  

  deputy.n.04                     0.417        0.518      0.000                  

  well.r.11                       0.376        0.54       0.000                  

  termination.n.05                0.187        0.666      0.000                  
  ---------------------------------------------------------------------------------------

  : . Difference in selection rate between titles

The full tables with analysis are shown in [Section 5.6](#_Comperison_of_synsets) and the [following link](https://docs.google.com/spreadsheets/d/1dcpC9uhsq7mT2R6a2YHX_1ezgtEx9iP_/edit?usp=sharing&ouid=102987810457035811283&rtpof=true&sd=true). The chart below shows the difference for selected synsets.

# Study 2

## Introduction

The previous phase demonstrated that certain words stimulate greater IE, yielding significantly higher scores for participation (action), perception (attitude), and perseverance (awareness). This second phase identifies textual predictors that are most effective in promoting IE and develops a strategy to systematically measure them. Based on the findings of the investigation into whether IE is determined by the text itself, specifically word choice, a novel framework was developed to identify engaging information strategically and systematically. The framework includes a predictive model of IE attributes as well as an instrument to measure and predict IE effectively and efficiently using computational linguistics**.**

The research questions that guide this phase are the following:

**R~1~: Which textual predictors drive IE?**

**R~2~: Can IE be systematically and automatically predicted?**

## Methods 

### Study Design

This study aimed to predict the probability that a word will be engaging based on its quantitative linguistic features. To do so, a list of 50 sets of synonyms, pairs of words that mean exactly or nearly the same, were compiled randomly from WordNet to obtain 100 words total. For a complete list of the words, see [Section 5.4](#_Word_pairs). As described in Chapter 2, the words were measured for IE in a large-scale user survey and classified with their means for participation (selection rate), perception (evaluation score), and perseverance (retention rate). The three IE dimensions for each word were computed by calculating the mean evaluation score based on the UES, the probability that a word would be selected, and the probability it would be remembered. [Appendix](#_IE_scores_for) A shows the words cores [and Appendix B shows all the data collected.](https://docs.google.com/spreadsheets/d/1A89-44kE-1XEuIJ785H3zR3gcW6cOCyL/edit?usp=sharing&ouid=108785364540065920816&rtpof=true&sd=true)

Text classifiers use machine learning, NLP, and text analysis to make classifications based on past observations. By using pre-labeled examples, a model based on such classifications can learn the associations between pieces of text to identify the outputs for a particular input. In this study, the input was *text* and the expected outputs were *tags*, pre-determined classifications for which any given piece of text could be categorized. This study uses the findings of Study 1 as classifiers.

For each word, textual features were automatically extracted based on the READ model. Then a series of multivariate linear regressions analyses were conducted to determine the associative and predictive significance of the recognized textual predictors for IE.

### Measurements 

The first step towards training an NLP classifier is *feature extraction,* a method used to transform each text into a numerical representation, also called a *vector*. For feature-selection calculation, we programmed an original program called [READ in Python (available here).](https://drive.google.com/file/d/1evESp3Ahj4pg9O474JxSaEvnKKl8OpDr/view?usp=sharing) The program was written using a suite of libraries for symbolic and statistical NLP, including the Natural Language Toolkit (NLTK), with the Python programming language (the program code is [available](https://drive.google.com/drive/folders/1dLch7_9Bcb3xDY24MmTO0foIkSKivovv?usp=sharing) here). The program accepts a word as input and returns quantitative data regarding the representative measures within the conceptual predictive model.

#### Representativeness measures  {#representativeness-measures .unnumbered}

Representativeness can be operationalized using semantic relation analysis, which calculates equivalency, hierarchy, and association. The following representativeness predictors were calculated:

1.  **Definitions (senses)**: A *sense* or definition is a discrete representation of one aspect of a word's meaning. *Polysemy* is the capacity for a word or phrase to have multiple meanings, usually related by contiguity of meaning within a semantic field. The polysemy count is the number of possible meanings of a word or phrase and is therefore the number of senses a word has. To count the number of senses (meanings), WordNet, a large lexical database of English phrases grouped into sets of cognitive synonyms (synsets) that each express a distinct concept, was used \[@miller1995\]. For example, the word "star" is associated with 12 different synsets (senses or meanings) in WordNet, whereas one of its synonyms, the word "maven," with only one. The mean definition score for all words was 7.85 (SD = 11).

2.  **Hypernyms:** A *hypernym* is a superordinate term under which more specific words fall. For example, the word "color" is a hypernym of "red" and "fruit" is a hypernym of "banana" and "mango." The mean number of hypernyms for each word in the study was 4.75 (SD =7.5).

3.  **Hyponyms:** A *hyponym* is a subordinate term that falls under one or more broader terms. *Hyponymy* or IS-A relation, the most frequently encoded relationship among synsets, links more general synsets like "furniture, piece of furniture" to increasingly specific ones like "bed" and "bunkbed." Thus, WordNet states that the category "furniture" includes "bed," which in turn includes "bunkbed"; conversely, concepts like "bed" and "bunkbed" make up the category "furniture." All noun hierarchies ultimately go up the root node (entity). For example, the words "banana" and "mango" are hyponyms (more specific concepts) for the word "fruit."

#### Ease-of-use Measures  {#ease-of-use-measures .unnumbered}

The following measures were used to assess the ease of understanding and using a word.

4.  **Length:** The complexity of a word was operationalized by calculating its length in terms of number of characters using NLTK. For example, the word "star" has a word length of 4 and "maven" of 5. The mean length of the words in the list was 6.58 (SD = 2.62).

5.  **Syllable count:** The number of syllables was counted as the total number of units of pronunciation with one vowel sound, with or without surrounding consonants, forming the whole or a part of a word. For example, "star" has one syllable and "maven" has two. The mean syllable count for the list was 2.17.

6.  **Flesch Reading Ease Score:** The Flesch Reading Ease Formula was developed to assess the ease with which a piece of text is understood and engaged. It provides a score between 1 and 100, with 100 being the highest readability score. A score between 70 and 80 is equivalent to a Grade 8 school level, at which text should be fairly easy for the average adult to read. While the maximum score is 121.22, there is no limit on the lowest score. Using Textstat[^4], an easy-to-use library, the Flesch Reading Ease scores were calculated for each word. The mean for the list was 36.6, SD = 89.98.

#### Affect Measures {#affect-measures .unnumbered}

7.  **Sentiment score:** Sentiment analysis, which aims at understanding and quantifying the sentiment of written text, was used to determine whether the wording of a text is positive, negative, or neutral. Using SentiWordNet 3.0, a lexical database based on WordNet, each word was assigned a sentiment score ranging from 0 to 1 \[@baccianellaSentiwordnetEnhancedLexical2010\]. Three types of sentiment scores, the positivity, negativity, and emotionality scores, were calculated for each word, with the positivity and negativity scores based on all the scores of the synsets associated with it and its overall emotionality score calculated by adding the positivity and negativity scores.

#### Distribution measures  {#distribution-measures .unnumbered}

8.  **Frequency:** Distribution was operationalized in terms of frequency using WordFreq, a Python library for identifying the frequency of words using data aggregated from the Exquisite Corpus,[^5] which compiles data from the following domains \[@speer2018\]:

```{=html}
<!-- -->
```
1.  Encyclopedic text from Wikipedia

2.  Subtitles from OPUS OpenSubtitles 2018 and SUBTLEX

3.  News from NewsCrawl 2014 and GlobalVoices

4.  Books from Google Books Ngrams 2012

5.  Web text from ParaCrawl, the Leeds Internet Corpus, and the MOKK Hungarian Webcorpus

6.  Short-form social media text from Twitter

7.  Long-form social media text from Reddit

For example, WordFreq assigns "star" a frequency score of 0.000129 and "maven" of 0.00000003.

9.  **Zipf frequency:** Zipf frequency, a variation on word frequency, is the base-10 logarithm of the number of times a word appears per billion words. For example, a word with a Zipf value of 6 appears once per 1,000 words and of 3 appears once per 1,000,000 words, with typical Zipf values between 0 and 8. For example, "star" has a Zipf value of 5.11 and "maven" of 1.48.

The table below summarizes the descriptive statistics for the 100 words.

  ------------------------- --------------- --------------- --------------- --------------- --------------- -------------------- --------------- --------------- ---------------- --------------- ----------------
                            **N**           **Range**       **Minimum**     **Maximum**     **Mean**        **Std. Deviation**   **Variance**    **Skewness**                     **Kurtosis**    

                            **Statistic**   **Statistic**   **Statistic**   **Statistic**   **Statistic**   **Statistic**        **Statistic**   **Statistic**   **Std. Error**   **Statistic**   **Std. Error**

  **N**                     80500           0               805             805             805.00          .000                 .000            .               .                .               .

  **definitions-synsets**   80500           69              1               70              7.85            10.989               120.769         3.168           .009             11.689          .017

  **hypernyms**             80500           60              0               60              4.75            7.495                56.168          4.564           .009             27.911          .017

  **hyponyms**              80500           403             0               403             26.41           70.015               4902.143        3.973           .009             16.265          .017

  **sylla**                 80500           5               1               6               2.17            1.141                1.301           .958            .009             .484            .017

  **len**                   80500           12              3               15              6.58            2.616                6.844           .741            .009             -.027           .017

  **flesch_reading_ease**   80500           423.01          -301.79         121.22          36.6172         89.53656             8016.796        -1.063          .009             1.050           .017

  **pos**                   80500           .875            .000            .875            .22000          .266999              .071            .954            .009             -.384           .017

  **neg**                   80500           .875            .000            .875            .19708          .264434              .070            .963            .009             -.543           .017

  **emotionality**          80500           1.000           .000            1.000           .35500          .320509              .103            .242            .009             -1.328          .017

  **emotionalitysum**       80500           1.500           .000            1.500           .41708          .401708              .161            .520            .009             -.859           .017

  **wnfreq**                80500           .00257          .00000          .00257          .0001394        .00035870            .000            4.235           .009             21.540          .017

  **wnzipf**                80500           6.41            .00             6.41            3.7731          1.39448              1.945           -.211           .009             -.697           .017

  **Valid N (listwise)**    80500                                                                                                                                                                 
  ------------------------- --------------- --------------- --------------- --------------- --------------- -------------------- --------------- --------------- ---------------- --------------- ----------------

  : . Difference in retention between titles

### Prediction and Evaluation 

Training data regarding the attributes of each word and tag were used in regression models to produce a *text classifier*, a type of classification/prediction model. The performance of the text classifier was evaluated using a cross-validation method and by performing multiple regression with the word attributes as independent variables. The text classifier was used to predict the probability that a word is engaging both in general and compared to its synonym. The predictions were compared to the IE values obtained in the previous study to determine whether the predictions were correct (i.e., the text classifier obtained true positives and true negatives) or incorrect (i.e., it obtained false positives and/or false negatives). The table below shows the descriptive statistics for the IE dimensions.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 5%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 5%" />
</colgroup>
<thead>
<tr class="header">
<th rowspan="2"></th>
<th><blockquote>
<p>N</p>
</blockquote></th>
<th><blockquote>
<p><strong>Range</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Minimum</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Maximum</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Sum</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Mean</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Std. Deviation</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Variance</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Skewness</strong></p>
</blockquote></th>
<th colspan="2"><blockquote>
<p><strong>Kurtosis</strong></p>
</blockquote></th>
</tr>
<tr class="odd">
<th><blockquote>
<p>Statistic</p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Std. Error</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Std. Error</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Statistic</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Std. Error</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>UESavg</strong></p>
</blockquote></td>
<td><blockquote>
<p>80500</p>
</blockquote></td>
<td><blockquote>
<p>4.000</p>
</blockquote></td>
<td><blockquote>
<p>1.000</p>
</blockquote></td>
<td><blockquote>
<p>5.000</p>
</blockquote></td>
<td><blockquote>
<p>196171.250</p>
</blockquote></td>
<td><blockquote>
<p>2.43691</p>
</blockquote></td>
<td><blockquote>
<p>.003092</p>
</blockquote></td>
<td><blockquote>
<p>.877390</p>
</blockquote></td>
<td><blockquote>
<p>.770</p>
</blockquote></td>
<td><blockquote>
<p>1.249</p>
</blockquote></td>
<td><blockquote>
<p>.009</p>
</blockquote></td>
<td><blockquote>
<p>.295</p>
</blockquote></td>
<td><blockquote>
<p>.017</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>select</strong></p>
</blockquote></td>
<td><blockquote>
<p>80500</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>17556</p>
</blockquote></td>
<td><blockquote>
<p>.22</p>
</blockquote></td>
<td><blockquote>
<p>.001</p>
</blockquote></td>
<td><blockquote>
<p>.413</p>
</blockquote></td>
<td><blockquote>
<p>.171</p>
</blockquote></td>
<td><blockquote>
<p>1.365</p>
</blockquote></td>
<td><blockquote>
<p>.009</p>
</blockquote></td>
<td><blockquote>
<p>-.136</p>
</blockquote></td>
<td><blockquote>
<p>.017</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>retention</strong></p>
</blockquote></td>
<td><blockquote>
<p>80500</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>6494</p>
</blockquote></td>
<td><blockquote>
<p>.08</p>
</blockquote></td>
<td><blockquote>
<p>.001</p>
</blockquote></td>
<td><blockquote>
<p>.272</p>
</blockquote></td>
<td><blockquote>
<p>.074</p>
</blockquote></td>
<td><blockquote>
<p>3.080</p>
</blockquote></td>
<td><blockquote>
<p>.009</p>
</blockquote></td>
<td><blockquote>
<p>7.484</p>
</blockquote></td>
<td><blockquote>
<p>.017</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Valid N (listwise)</strong></p>
</blockquote></td>
<td><blockquote>
<p>80500</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

## Results

### H~1~: A word's representativeness, ease-of-use, affect, and distribution scores predict its IE levels {#h1-a-words-representativeness-ease-of-use-affect-and-distribution-scores-predict-its-ie-levels .unnumbered}

Multiple hierarchical linear regressions were run to predict a word's IE scores from its textual features. Feature associations were measured by performing linear regression analysis with IE as the dependent variable and the READ features as the independent variables.

  ----------------------------------------------------------------------------
  Variable                  *B*        *SE B*    *β*       t         p
  ------------------------- ---------- --------- --------- --------- ---------
  **(Constant)**            2.297      0.005               443.730   0.000

  **definitions-synsets**   0.000      0.000     -0.003    -0.704    0.481

  **hypernyms**             -0.005     0.000     -0.185    -40.455   0.000

  **hyponyms**              0.000      0.000     0.034     12.669    0.000

  **posmax**                0.126      0.005     0.161     23.911    0.000

  **emotionalitymax**       0.047      0.006     0.073     8.084     0.000

  **negmax**                -0.113     0.005     -0.143    -24.326   0.000

  **len**                   -0.019     0.001     -0.241    -36.046   0.000

  **flesch_reading_ease**   -0.001     0.000     -0.328    -51.952   0.000

  **sylla**                 -0.041     0.001     -0.223    -32.292   0.000

  **wnzipf**                0.108      0.001     0.722     177.654   0.000

  **wnfreq**                -175.563   1.842     -0.302    -95.297   0.000
  ----------------------------------------------------------------------------

*R2 = .539*

*F = 8542.284 (p=0)*

  ----------------------------------------------------------------------------------
  **Variable**              **B**       **SE B**   β              **t**     **p**
  ------------------------- ----------- ---------- -------------- --------- --------
  **(Constant)**            .207        .001                      386.743   .000

  **hypernyms**             .001        .000       .292           51.891    .000

  **hyponyms**              -4.169E-6   .000       -.017          -5.073    .000

  **definitions-synsets**   .000        .000       -.233          -39.534   .000

  **emotionalitymax2**      .028        .001       .513           47.049    .000

  **emotionalitysum**       -.021       .000       -.473          -43.413   .000

  **len**                   -.001       .000       -.112          -13.750   .000

  **flesch_reading_ease**   2.634E-6    .000       .013           1.719     .086

  **sylla**                 -.002       .000       -.115          -13.593   .000

  **wnzipf**                .005        .000       .419           85.397    .000

  **wnfreq**                -12.777     .187       -.260          -68.201   .000
  ----------------------------------------------------------------------------------

*R2 = .298*

*F = 3413.447 (p=0)*

  ------------------------- ----------- ---------- -------------- --------- ---------
  **Variable**              **B**       **SE B**   **β**          **t**     **p**

  **(Constant)**            .078        .000                      179.411   .000

  **definitions-synsets**   7.041E-5    .000       .058           8.888     .000

  **hyponyms**              -9.664E-6   .000       -.051          -14.206   .000

  **hypernyms**             -5.481E-5   .000       -.031          -5.107    .000

  **negmax2**               -.009       .000       -.183          -23.391   .000

  **emotionalitymax2**      .014        .000       .333           27.917    .000

  **posmax2**               -.014       .000       -.283          -31.612   .000

  **len**                   -.002       .000       -.298          -33.506   .000

  **flesch_reading_ease**   -8.185E-6   .000       -.055          -6.607    .000

  **sylla**                 .001        .000       .055           5.978     .000

  **wnzipf**                .003        .000       .337           62.357    .000

  **wnfreq**                -6.569      .155       -.178          -42.279   .000
  ------------------------- ----------- ---------- -------------- --------- ---------

*R2 = .185*

*F = 1663.846 (p=0)*

All the standardized coefficients were significant for all the predictive variables. The tables and figures below show the residual statistics for the three IE levels.

+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > *Residual Statistics^a^*              |                     |                     |                     |                      |         |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
|                                         | > **Minimum**       | > **Maximum**       | > **Mean**          | > **Std. Deviation** | > **N** |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Predicted Value**                   | > 2.028855562210083 | > 2.712723493576050 | > 2.436909937888200 | > .154166730259890   | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Std. Predicted Value**              | > -2.647            | > 1.789             | > .000              | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Standard Error of Predicted Value** | > .001              | > .004              | > .002              | > .001               | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Adjusted Predicted Value**          | > 2.028802871704102 | > 2.712774515151978 | > 2.436910428212415 | > .154168383244428   | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Residual**                          | > -.322816610336304 | > .449359506368637  | > -.000000000000001 | > .140292228270305   | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Std. Residual**                     | > -2.301            | > 3.203             | > .000              | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Std. Residual**                     | > -2.301            | > 3.203             | > .000              | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Deleted Residual**                  | > -.322835564613342 | > .449377685785294  | > -.000000490324215 | > .140308968871233   | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Std. Deleted Residual**             | > -2.301            | > 3.203             | > .000              | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Mahal. Distance**                   | > 1.159             | > 68.616            | > 12.000            | > 11.479             | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Cook\'s Distance**                  | > .000              | > .000              | > .000              | > .000               | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > **Centered Leverage Value**           | > .000              | > .001              | > .000              | > .000               | > 80500 |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+
| > a\. Dependent variable: M~UES~        |                     |                     |                     |                      |         |
+-----------------------------------------+---------------------+---------------------+---------------------+----------------------+---------+

![](./assets/media/image5.png){width="6.752969160104987in" height="3.9716983814523186in"}

Figure . Normal P-P Plot of Regression Standardized Residual

+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
|                                         | > **Minimum**       | > **Maximum**      | > **Mean**         | > **Std. Deviation** | > **N** |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
|                                         |                     |                    |                    |                      |         |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Predicted Value**                   | > .191425189375877  | > .239431917667389 | > .218086956521739 | > .009707254801688   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Predicted Value**              | > -2.747            | > 2.199            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Standard Error of Predicted Value** | > .000              | > .000             | > .000             | > .000               | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Adjusted Predicted Value**          | > .191421255469322  | > .239440575242043 | > .218086951859593 | > .009707267525310   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Residual**                          | > -.031844928860664 | > .048527769744396 | > .000000000000000 | > .014701745903071   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Residual**                     | > -2.166            | > 3.301            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Residual**                     | > -2.166            | > 3.301            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Deleted Residual**                  | > -.031847275793552 | > .048529680818319 | > .000000004662146 | > .014703630227295   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Deleted Residual**             | > -2.166            | > 3.301            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Mahal. Distance**                   | > 1.122             | > 63.069           | > 11.000           | > 10.894             | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Cook\'s Distance**                  | > .000              | > .000             | > .000             | > .000               | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Centered Leverage Value**           | > .000              | > .001             | > .000             | > .000               | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > a\. Dependent variable: Mselect       |                     |                    |                    |                      |         |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+

![A picture containing chart Description automatically generated](./assets/media/image6.png){width="8.14713910761155in" height="4.791666666666667in"}

Figure . Normal P-P Plot of Regression Standardized Residual

+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > *Residual Statistics^a^*              |                     |                    |                    |                      |         |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
|                                         | > **Minimum**       | > **Maximum**      | > **Mean**         | > **Std. Deviation** | > **N** |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Predicted Value**                   | > .064031764864922  | > .092496223747730 | > .080670807453416 | > .005802692796775   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Predicted Value**              | > -2.867            | > 2.038            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Standard Error of Predicted Value** | > .000              | > .000             | > .000             | > .000               | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Adjusted Predicted Value**          | > .064033478498459  | > .092493295669556 | > .080670752521956 | > .005802638012662   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Residual**                          | > -.023946253582835 | > .054042458534241 | > .000000000000000 | > .011887750984499   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Residual**                     | > -2.014            | > 4.546            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Residual**                     | > -2.014            | > 4.546            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Deleted Residual**                  | > -.023947916924953 | > .054044622927904 | > .000000054931460 | > .011889142183245   | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Std. Deleted Residual**             | > -2.014            | > 4.546            | > .000             | > 1.000              | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Mahal. Distance**                   | > .943              | > 68.474           | > 11.000           | > 11.380             | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Cook\'s Distance**                  | > .000              | > .000             | > .000             | > .000               | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > **Centered Leverage Value**           | > .000              | > .001             | > .000             | > .000               | > 80500 |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+
| > a\. Dependent variable: Mreten        |                     |                    |                    |                      |         |
+-----------------------------------------+---------------------+--------------------+--------------------+----------------------+---------+

![Chart Description automatically generated with low confidence](./assets/media/image7.png){width="7.904086832895888in" height="4.6605391513560805in"}

Figure . Normal P-P Plot of Regression Standardized Residual

The results confirm that a word's IE dimensions can be predicted systematically based on its textual factors.

All the case-wise diagnostics for the specific words are shown in [Section 6.2.1](#_Linear_regression_models).

### H~2~: When there is more than one possible word to describe the same information, a word's representativeness, ease-of-use, affect. and distribution scores will predict whether a synonym is more engaging  {#h2-when-there-is-more-than-one-possible-word-to-describe-the-same-information-a-words-representativeness-ease-of-use-affect.-and-distribution-scores-will-predict-whether-a-synonym-is-more-engaging-1 .unnumbered}

Using the prediction scores shown in the previous section, the synonyms were compared to predict which one would have higher perception, participation, and perseverance scores. For perception as measured by mean UES, the model was correct in **[100% of the cases]{.underline}**, i.e., the model was able to correctly predict which synonym would have a higher UES score for all 50 synsets. The table below shows the observed and predicted values.

  -------------------------------------------------------------------------------
  **Synset/word**            **Observed** x̄ **ues**    **Predicted** x̄ UES
  -------------------------- ------------------------- --------------------------
  **abused.a.02**            **2.270574534**           **2.316106483**

  abused                     2.30931677                2.40796335

  maltreated                 2.231832298               2.224249616

  **ace.n.03**               **2.508229814**           **2.392164589**

  maven                      2.188975155               2.175973693

  star                       2.827484472               2.608355485

  **agile.s.01**             **2.501164596**           **2.531099669**

  nimble                     2.346428571               2.455531433

  quick                      2.655900621               2.606667905

  **ample.s.02**             **2.640916149**           **2.422189894**

  plenteous                  2.214130435               2.174203384

  rich                       3.067701863               2.670176404

  **annoying.s.01**          **2.33439441**            **2.269335175**

  annoying                   2.472360248               2.435186412

  nettlesome                 2.196428571               2.103483937

  **art.n.03**               **2.582142857**           **2.582653239**

  art                        2.816770186               2.687286894

  prowess                    2.347515528               2.478019584

  **asleep.s.03**            **2.379968944**           **2.411206234**

  deceased                   2.365062112               2.378956003

  gone                       2.394875776               2.443456466

  **automaton.n.01**         **2.630512422**           **2.385718916**

  automaton                  2.347826087               2.307598588

  zombie                     2.913198758               2.463839244

  **avaricious.s.01**        **2.337111801**           **2.294853681**

  avaricious                 2.204658385               2.135496669

  greedy                     2.469565217               2.454210693

  **baron.n.03**             **2.556987578**           **2.481533586**

  king                       2.889906832               2.596783296

  magnate                    2.224068323               2.366283875

  **beget.v.01**             **2.471040373**           **2.449272212**

  engender                   2.209161491               2.320283668

  mother                     2.732919255               2.578260755

  **burp.v.01**              **2.347826087**           **2.350340638**

  belching                   2.243012422               2.266681578

  bubbling                   2.452639752               2.433999699

  **combatant.n.01**         **2.527717391**           **2.384452056**

  belligerent                2.433074534               2.282070963

  fighter                    2.622360248               2.48683315

  **computerization.n.01**   **2.330512422**           **2.128551765**

  computerization            2.351397516               2.228248077

  cybernation                2.309627329               2.028855453

  **cut.s.03**               **2.331677019**           **2.404329818**

  cut                        2.460093168               2.442048167

  shortened                  2.20326087                2.366611469

  **dame.n.02**              **2.548369565**           **2.443844305**

  gentlewoman                2.436180124               2.255865359

  lady                       2.660559006               2.631823252

  **death.n.04**             **2.638586957**           **2.492023102**

  death                      2.964130435               2.589851858

  demise                     2.313043478               2.394194346

  **departure.n.01**         **2.380357143**           **2.426419985**

  departure                  2.311024845               2.4578919

  going                      2.449689441               2.394948071

  **deputy.n.04**            **2.289208075**           **2.433813409**

  deputy                     2.277484472               2.471227436

  surrogate                  2.300931677               2.396399382

  **discovery.n.01**         **2.34363354**            **2.471357072**

  find                       2.451242236               2.599334094

  uncovering                 2.236024845               2.343380049

  **dove.n.02**              **2.364518634**           **2.31150645**

  dove                       2.536956522               2.488760431

  peacenik                   2.192080745               2.134252469

  **dress.v.16**             **2.371350932**           **2.434022805**

  coif                       2.202950311               2.299637225

  done                       2.539751553               2.568408385

  **enemy.n.02**             **2.397903727**           **2.542061534**

  enemy                      2.48121118                2.597208522

  opposition                 2.314596273               2.486914546

  **epicure.n.01**           **2.462965839**           **2.352942363**

  epicurean                  2.223447205               2.279237567

  foodie                     2.702484472               2.426647159

  **exile.n.02**             **2.294254658**           **2.366151322**

  deportee                   2.18136646                2.240271044

  exile                      2.407142857               2.4920316

  **exuberant.s.03**         **2.368012422**           **2.390322862**

  lush                       2.497204969               2.48092207

  profuse                    2.238819876               2.299723654

  **gluey.s.01**             **2.275698758**           **2.206571379**

  mucilaginous               2.17826087                2.034911827

  sticky                     2.373136646               2.378230932

  **hit.n.03**               **2.386257764**           **2.464690747**

  hit                        2.45326087                2.557341081

  smasher                    2.319254658               2.372040414

  **ill.r.01**               **2.41878882**            **2.538871348**

  ill                        2.510093168               2.608241817

  poorly                     2.327484472               2.469500879

  **immediately.r.01**       **2.368944099**           **2.405754036**

  forthwith                  2.193944099               2.306559318

  now                        2.543944099               2.504948753

  **interchange.n.02**       **2.341770186**           **2.28584758**

  interchange                2.301863354               2.336182789

  reciprocation              2.381677019               2.23551237

  **lifelike.s.02**          **2.592391304**           **2.525181886**

  lifelike                   2.421118012               2.436725885

  natural                    2.763664596               2.613637886

  **merely.r.01**            **2.32810559**            **2.496791647**

  just                       2.438043478               2.452598997

  merely                     2.218167702               2.540984297

  **motivation.n.01**        **2.553416149**           **2.522165532**

  motive                     2.570341615               2.47795561

  need                       2.536490683               2.566375455

  **organism.n.01**          **2.437034161**           **2.51342651**

  being                      2.465372671               2.599966976

  organism                   2.408695652               2.426886043

  **pale.v.01**              **2.269953416**           **2.422024179**

  blanch                     2.161801242               2.323185248

  pale                       2.37810559                2.520863109

  **pant.v.01**              **2.414130435**           **2.431515167**

  gasp                       2.370031056               2.44117104

  puff                       2.458229814               2.421859295

  **person.n.01**            **2.670652174**           **2.59533705**

  mortal                     2.536645963               2.527682153

  soul                       2.804658385               2.662991947

  **pirate.n.02**            **2.40628882**            **2.385958899**

  buccaneer                  2.334627329               2.291885807

  pirate                     2.477950311               2.480031991

  **preen.v.03**             **2.379968944**           **2.366763247**

  dress                      2.525621118               2.511254909

  primp                      2.23431677                2.222271584

  **putrefaction.n.01**      **2.300854037**           **2.342991187**

  putrefaction               2.205590062               2.240374402

  rot                        2.396118012               2.445607971

  **real.s.04**              **2.619953416**           **2.602621777**

  real                       2.76568323                2.639113004

  tangible                   2.474223602               2.566130551

  **sex.n.04**               **2.852173913**           **2.614759287**

  gender                     2.594720497               2.559053182

  sex                        3.109627329               2.670465391

  **termination.n.05**       **2.350854037**           **2.466347131**

  ending                     2.342391304               2.5290575

  termination                2.35931677                2.403636762

  **veracious.s.02**         **2.404037267**           **2.481133452**

  right                      2.590372671               2.636433811

  veracious                  2.217701863               2.325833093

  **wash.v.02**              **2.341537267**           **2.438021134**

  lave                       2.208850932               2.316743774

  wash                       2.474223602               2.559298494

  **well.r.03**              **2.651164596**           **2.703051391**

  best                       2.787267081               2.710026623

  easily                     2.515062112               2.69607616

  **well.r.11**              **2.597903727**           **2.689484998**

  better                     2.612888199               2.712723464

  well                       2.582919255               2.666246531

  **wiccan.n.01**            **2.352096273**           **2.40227664**

  wiccan                     2.245496894               2.348621388

  witch                      2.458695652               2.455931892

  **witness.n.01**           **2.321583851**           **2.475637529**

  informant                  2.282298137               2.405917933

  witness                    2.360869565               2.545357125

                                                       
  -------------------------------------------------------------------------------

For participation as measured by selection rate, the model was correct in 84**[% of the cases,]{.underline} i.e.,** the model was able to correctly predict which synonym would have a higher selection rate in 42 of the 50 synsets. The table below shows the observed and predicted values.

  ---------------------------------------------------------------------------------------
  **Synset/word**            **Observed selection rate**   **Predicted selection rate**
  -------------------------- ----------------------------- ------------------------------
  **abused.a.02**            **0.219875776**               **0.212782391**

  abused                     0.222360248                   0.216821613

  maltreated                 0.217391304                   0.208743169

  **ace.n.03**               **0.235403727**               **0.220889565**

  maven                      0.21863354                    0.207676142

  star                       0.252173913                   0.234102988

  **agile.s.01**             **0.203726708**               **0.223021323**

  nimble                     0.196273292                   0.21776663

  quick                      0.211180124                   0.228276016

  **ample.s.02**             **0.206832298**               **0.21464143**

  plenteous                  0.172670807                   0.204515735

  rich                       0.240993789                   0.224767125

  **annoying.s.01**          **0.223602484**               **0.209729781**

  annoying                   0.217391304                   0.218602194

  nettlesome                 0.229813665                   0.200857367

  **art.n.03**               **0.230434783**               **0.227259772**

  art                        0.253416149                   0.23395339

  prowess                    0.207453416                   0.220566155

  **asleep.s.03**            **0.207453416**               **0.221747954**

  deceased                   0.203726708                   0.219167507

  gone                       0.211180124                   0.224328401

  **automaton.n.01**         **0.244099379**               **0.21368329**

  automaton                  0.21863354                    0.206329131

  zombie                     0.269565217                   0.221037449

  **avaricious.s.01**        **0.21552795**                **0.212789599**

  avaricious                 0.217391304                   0.202851813

  greedy                     0.213664596                   0.222727384

  **baron.n.03**             **0.209937888**               **0.222097515**

  king                       0.231055901                   0.229939519

  magnate                    0.188819876                   0.21425551

  **beget.v.01**             **0.224223602**               **0.218239391**

  engender                   0.197515528                   0.209391304

  mother                     0.250931677                   0.227087477

  **burp.v.01**              **0.22484472**                **0.216384689**

  belching                   0.217391304                   0.212061376

  bubbling                   0.232298137                   0.220708002

  **combatant.n.01**         **0.219875776**               **0.214760391**

  belligerent                0.216149068                   0.207196916

  fighter                    0.223602484                   0.222323866

  **computerization.n.01**   **0.20621118**                **0.193862166**

  computerization            0.2                           0.196299147

  cybernation                0.21242236                    0.191425185

  **cut.s.03**               **0.226086957**               **0.227427506**

  cut                        0.228571429                   0.239431921

  shortened                  0.223602484                   0.215423091

  **dame.n.02**              **0.220496894**               **0.215516643**

  gentlewoman                0.214906832                   0.203372913

  lady                       0.226086957                   0.227660373

  **death.n.04**             **0.229192547**               **0.226619241**

  death                      0.260869565                   0.234705961

  demise                     0.197515528                   0.218532521

  **departure.n.01**         **0.21242236**                **0.22060375**

  departure                  0.217391304                   0.219963823

  going                      0.207453416                   0.221243676

  **deputy.n.04**            **0.229813665**               **0.218909848**

  deputy                     0.234782609                   0.224670824

  surrogate                  0.22484472                    0.213148871

  **discovery.n.01**         **0.220496894**               **0.220170333**

  find                       0.228571429                   0.232458163

  uncovering                 0.21242236                    0.207882502

  **dove.n.02**              **0.200621118**               **0.215973497**

  dove                       0.213664596                   0.225753802

  peacenik                   0.18757764                    0.206193193

  **dress.v.16**             **0.22484472**                **0.220340725**

  coif                       0.231055901                   0.214917735

  done                       0.21863354                    0.225763715

  **enemy.n.02**             **0.222981366**               **0.223422013**

  enemy                      0.236024845                   0.223309078

  opposition                 0.209937888                   0.223534948

  **epicure.n.01**           **0.213043478**               **0.212565765**

  epicurean                  0.191304348                   0.207438343

  foodie                     0.234782609                   0.217693188

  **exile.n.02**             **0.208074534**               **0.213100728**

  deportee                   0.202484472                   0.204640762

  exile                      0.213664596                   0.221560693

  **exuberant.s.03**         **0.217391304**               **0.218648114**

  lush                       0.236024845                   0.225646717

  profuse                    0.198757764                   0.211649511

  **gluey.s.01**             **0.220496894**               **0.206619963**

  mucilaginous               0.207453416                   0.195009667

  sticky                     0.233540373                   0.218230259

  **hit.n.03**               **0.225465839**               **0.221390506**

  hit                        0.232298137                   0.22589545

  smasher                    0.21863354                    0.216885562

  **ill.r.01**               **0.219875776**               **0.226068431**

  ill                        0.226086957                   0.228878354

  poorly                     0.213664596                   0.223258508

  **immediately.r.01**       **0.228571429**               **0.212234468**

  forthwith                  0.219875776                   0.213688959

  now                        0.237267081                   0.210779977

  **interchange.n.02**       **0.225465839**               **0.207409057**

  interchange                0.236024845                   0.21439872

  reciprocation              0.214906832                   0.200419394

  **lifelike.s.02**          **0.209937888**               **0.217058638**

  lifelike                   0.21863354                    0.217991482

  natural                    0.201242236                   0.216125793

  **merely.r.01**            **0.197515528**               **0.213827603**

  just                       0.19378882                    0.205889643

  merely                     0.201242236                   0.221765563

  **motivation.n.01**        **0.205590062**               **0.222144174**

  motive                     0.198757764                   0.219787407

  need                       0.21242236                    0.224500942

  **organism.n.01**          **0.21242236**                **0.216772802**

  being                      0.213664596                   0.218894372

  organism                   0.211180124                   0.214651233

  **pale.v.01**              **0.201863354**               **0.216549566**

  blanch                     0.202484472                   0.215559274

  pale                       0.201242236                   0.217539859

  **pant.v.01**              **0.227329193**               **0.224299509**

  gasp                       0.21863354                    0.221835169

  puff                       0.236024845                   0.22676385

  **person.n.01**            **0.237888199**               **0.228108713**

  mortal                     0.22484472                    0.22080355

  soul                       0.250931677                   0.235413875

  **pirate.n.02**            **0.206832298**               **0.215599514**

  buccaneer                  0.20621118                    0.208195201

  pirate                     0.207453416                   0.223003827

  **preen.v.03**             **0.222360248**               **0.220658939**

  dress                      0.242236025                   0.231835056

  primp                      0.202484472                   0.209482823

  **putrefaction.n.01**      **0.208695652**               **0.209273268**

  putrefaction               0.182608696                   0.196011665

  rot                        0.234782609                   0.222534872

  **real.s.04**              **0.226708075**               **0.219537332**

  real                       0.242236025                   0.218731285

  tangible                   0.211180124                   0.220343378

  **sex.n.04**               **0.238509317**               **0.228828999**

  gender                     0.226086957                   0.224064941

  sex                        0.250931677                   0.233593057

  **termination.n.05**       **0.195652174**               **0.218859779**

  ending                     0.20621118                    0.224971311

  termination                0.185093168                   0.212748246

  **veracious.s.02**         **0.219875776**               **0.214754846**

  right                      0.233540373                   0.219831595

  veracious                  0.20621118                    0.209678096

  **wash.v.02**              **0.222360248**               **0.22607741**

  lave                       0.20621118                    0.215029099

  wash                       0.238509317                   0.23712572

  **well.r.03**              **0.213664596**               **0.221652034**

  best                       0.213664596                   0.217146804

  easily                     0.213664596                   0.226157264

  **well.r.11**              **0.218012422**               **0.220130496**

  better                     0.227329193                   0.215687149

  well                       0.208695652                   0.224573844

  **wiccan.n.01**            **0.213043478**               **0.219889652**

  wiccan                     0.202484472                   0.212473665

  witch                      0.223602484                   0.227305639

  **witness.n.01**           **0.208695652**               **0.221414706**

  informant                  0.192546584                   0.214989744

  witness                    0.22484472                    0.227839669
  ---------------------------------------------------------------------------------------

For perseverance as measured by retention rate, the model was correct [**in 80% of the cases**,]{.underline} i.e., the model was able to correctly predict which synonym would have a higher retention rate in 40 of the 50 synsets. Table 13 shows the observed and predicted values.

  -----------------------------------------------------------------------
  **Synset / word**          **Retention rate**    **Prediction rate**
  -------------------------- --------------------- ----------------------
  **abused.a.02**            **0.079503106**       **0.077865209**

  abused                     0.089440994           0.079403141

  maltreated                 0.069565217           0.076327277

  **ace.n.03**               **0.077639752**       **0.080240714**

  maven                      0.072049689           0.074186197

  star                       0.083229814           0.086295232

  **agile.s.01**             **0.065838509**       **0.083470796**

  nimble                     0.068322981           0.079641301

  quick                      0.063354037           0.087300292

  **ample.s.02**             **0.079503106**       **0.079053551**

  plenteous                  0.067080745           0.071861001

  rich                       0.091925466           0.086246102

  **annoying.s.01**          **0.07826087**        **0.076222273**

  annoying                   0.070807453           0.08195422

  nettlesome                 0.085714286           0.070490325

  **art.n.03**               **0.07826087**        **0.083926062**

  art                        0.093167702           0.088402875

  prowess                    0.063354037           0.07944925

  **asleep.s.03**            **0.086956522**       **0.081259837**

  deceased                   0.072049689           0.079880612

  gone                       0.101863354           0.082639062

  **automaton.n.01**         **0.111180124**       **0.078411236**

  automaton                  0.085714286           0.074218968

  zombie                     0.136645963           0.082603504

  **avaricious.s.01**        **0.080124224**       **0.077496549**

  avaricious                 0.072049689           0.072319685

  greedy                     0.088198758           0.082673414

  **baron.n.03**             **0.08757764**        **0.082575181**

  king                       0.09068323            0.087240578

  magnate                    0.08447205            0.077909783

  **beget.v.01**             **0.08136646**        **0.081273863**

  engender                   0.062111801           0.076324925

  mother                     0.100621118           0.086222801

  **burp.v.01**              **0.075776398**       **0.075741386**

  belching                   0.064596273           0.075011343

  bubbling                   0.086956522           0.07647143

  **combatant.n.01**         **0.088819876**       **0.078165468**

  belligerent                0.07826087            0.074438044

  fighter                    0.099378882           0.081892892

  **computerization.n.01**   **0.072049689**       **0.06761581**

  computerization            0.070807453           0.069285909

  cybernation                0.073291925           0.065945711

  **cut.s.03**               **0.08757764**        **0.082460575**

  cut                        0.089440994           0.087690387

  shortened                  0.085714286           0.077230763

  **dame.n.02**              **0.099378882**       **0.079908161**

  gentlewoman                0.09689441            0.071689513

  lady                       0.101863354           0.088126809

  **death.n.04**             **0.105590062**       **0.086333253**

  death                      0.131677019           0.09115215

  demise                     0.079503106           0.081514355

  **departure.n.01**         **0.073291925**       **0.082446037**

  departure                  0.075776398           0.082171491

  going                      0.070807453           0.082720584

  **deputy.n.04**            **0.081987578**       **0.081921006**

  deputy                     0.074534161           0.085563039

  surrogate                  0.089440994           0.078278973

  **discovery.n.01**         **0.068322981**       **0.079971875**

  find                       0.070807453           0.084068473

  uncovering                 0.065838509           0.075875276

  **dove.n.02**              **0.080124224**       **0.07854873**

  dove                       0.088198758           0.084905714

  peacenik                   0.072049689           0.072191745

  **dress.v.16**             **0.07826087**        **0.08193058**

  coif                       0.081987578           0.077843701

  done                       0.074534161           0.086017459

  **enemy.n.02**             **0.080745342**       **0.087423229**

  enemy                      0.08447205            0.087945047

  opposition                 0.077018634           0.086901411

  **epicure.n.01**           **0.076397516**       **0.076495241**

  epicurean                  0.075776398           0.074311461

  foodie                     0.077018634           0.07867902

  **exile.n.02**             **0.07515528**        **0.079238789**

  deportee                   0.077018634           0.074331812

  exile                      0.073291925           0.084145766

  **exuberant.s.03**         **0.080745342**       **0.081435513**

  lush                       0.093167702           0.084880312

  profuse                    0.068322981           0.077990714

  **gluey.s.01**             **0.074534161**       **0.075838798**

  mucilaginous               0.07826087            0.067897881

  sticky                     0.070807453           0.083779715

  **hit.n.03**               **0.078881988**       **0.077801596**

  hit                        0.072049689           0.081001661

  smasher                    0.085714286           0.074601532

  **ill.r.01**               **0.091925466**       **0.089882937**

  ill                        0.108074534           0.092496227

  poorly                     0.075776398           0.087269647

  **immediately.r.01**       **0.080124224**       **0.079400171**

  forthwith                  0.065838509           0.077007324

  now                        0.094409938           0.081793018

  **interchange.n.02**       **0.073913043**       **0.073167206**

  interchange                0.074534161           0.075108474

  reciprocation              0.073291925           0.071225938

  **lifelike.s.02**          **0.080124224**       **0.080483361**

  lifelike                   0.069565217           0.075975191

  natural                    0.09068323            0.084991532

  **merely.r.01**            **0.076397516**       **0.079944477**

  just                       0.079503106           0.075779386

  merely                     0.073291925           0.084109569

  **motivation.n.01**        **0.086335404**       **0.083731389**

  motive                     0.094409938           0.083268961

  need                       0.07826087            0.084193818

  **organism.n.01**          **0.080124224**       **0.083203739**

  being                      0.07826087            0.08499351

  organism                   0.081987578           0.081413968

  **pale.v.01**              **0.073913043**       **0.079584835**

  blanch                     0.075776398           0.077768644

  pale                       0.072049689           0.081401027

  **pant.v.01**              **0.077018634**       **0.083153075**

  gasp                       0.072049689           0.083790814

  puff                       0.081987578           0.082515337

  **person.n.01**            **0.08757764**        **0.084002185**

  mortal                     0.08447205            0.081920315

  soul                       0.09068323            0.086084055

  **pirate.n.02**            **0.073291925**       **0.079130737**

  buccaneer                  0.075776398           0.075105553

  pirate                     0.070807453           0.08315592

  **preen.v.03**             **0.072049689**       **0.078498775**

  dress                      0.09068323            0.081647928

  primp                      0.053416149           0.075349622

  **putrefaction.n.01**      **0.073291925**       **0.074299065**

  putrefaction               0.059627329           0.064031764

  rot                        0.086956522           0.084566367

  **real.s.04**              **0.085093168**       **0.083870035**

  real                       0.079503106           0.087138234

  tangible                   0.09068323            0.080601835

  **sex.n.04**               **0.1**               **0.086517762**

  gender                     0.094409938           0.085045804

  sex                        0.105590062           0.08798972

  **termination.n.05**       **0.069565217**       **0.080485247**

  ending                     0.07826087            0.084080221

  termination                0.060869565           0.076890274

  **veracious.s.02**         **0.07515528**        **0.077550151**

  right                      0.081987578           0.084009738

  veracious                  0.068322981           0.071090565

  **wash.v.02**              **0.07826087**        **0.082511872**

  lave                       0.079503106           0.079415003

  wash                       0.077018634           0.085608742

  **well.r.03**              **0.088198758**       **0.087697949**

  best                       0.100621118           0.088708321

  easily                     0.075776398           0.086687577

  **well.r.11**              **0.07826087**        **0.087880044**

  better                     0.07                  0.087625386

  well                       0.07826087            0.088134701

  **wiccan.n.01**            **0.07826087**        **0.082660804**

  wiccan                     0.077018634           0.078972464

  witch                      0.079503106           0.086349144

  **witness.n.01**           **0.070807453**       **0.080813236**

  informant                  0.07                  0.078559468

  witness                    0.070807453           0.083067004
  -----------------------------------------------------------------------

# Study 3

## Introduction

This third and last study is a culmination of the previous two studies investigating the relationship between IE and information design and the key factors that predict IE. In this research phase, the findings of the previous two studies were combined to develop a prescriptive model and test it in large user studies. To do so, a list of article titles was compiled, and each title tokenized (broken down) into individual linguistic units (words) for evaluation of engagement using the READ Model that had been developed in Study 2. Using WordNet, words in the titles were matched with lists of (a) synonyms; (b) hypernyms, generic terms used to designate an entire class of specific instances; and (c) coordinate words, sister terms representing words that have the same hypernym. All the words were evaluated to obtain an IE score using the READ Model. Words that were predicted to be more engaging were used to replace the original words, a process called *synonym substitution*, and thereby manipulate the titles. The ‎original (control) and modified (treatment) titles were compared in a between-group design study (A/B testing) based on the measurement model developed in Study 1.

The expected results were that use of the more engaging words would produce titles with higher IE scores compared to use of the less engaging words in the titles. If these results were obtained, they would provide empirical support that IE is ‎fostered by, and perhaps dependent upon, information design, specifically the wording used, and thereby indicating that IE can be systematically evaluated, created, and enhanced.

## Measures

### Study Design

A randomized between-group design was employed to observe how changes in wording (the independent variable) impacted IE (the dependent variable). A list of article titles was manipulated by substituting words with synonyms selected based on their READ score. IE with the ‎original (control) and modified (treatment) titles was compared using a between-group design (A/B testing) based on measurement of perception, participation (selection), and perseverance (retention) using the UES.

### Preparing a READ Dataset

Based on the findings of the previous studies, the READ Model was developed as a means of providing the READ Score, a measurement of IE probability that was determined for each of the 155,287 words in WordNet \[@princetonuniversityWordNet2018\]. Using the READ database, each word in a search title was substituted with a synonym predicted to be more engaging as measured by participation, perception, and perseverance values. Verification that the substitution of a word does not alter the meaning of the text was performed manually. Candidate words were identified and replaced candidate with sticky words using the automatic system in the titles of eight news articles from *The New York Times* and *The Wall Street Journal*. [Chosen because The AllSides Media Bias Chart]{.mark}[^6] [helps you to easily identify different perspectives and political leanings in the news so you can get the full picture and think for yourself.]{.mark}

[Knowing the political bias of media outlets allows you to consume a balanced news diet and avoid manipulation, misinformation, and fake news. Everyone is biased, but hidden media bias misleads and divides us. The AllSides Media Bias Chart™ is based on our full and growing list of over 1,400 media bias ratings. These ratings inform our balanced newsfeed.]{.mark}

![Bias Media](./assets/media/image8.jpeg){width="6.4375in" height="5.0993055555555555in"}

It is important to highlight that only one word in each title was replaced with a potentially more engaging synonym, therefore controlling for all other variables. The result was the dataset of control and treatment (modified) titles shown in the table below.

  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
      **Original**                                                                                                                     **Modified**
  --- -------------------------------------------------------------------------------------------------------------------------------- ---------------------------------------------------------------------------------------------------------------------------
  1   Meet the web Metrics Mavens: How they got to where they are now, and what kinds of things they measure                           Meet the web Metrics Stars: How they got to where they are now, and what kinds of things they measure

  2   Staying Nimble: How Small Businesses Can, and Do, Shift Gears                                                                    Staying Quick: How Small Businesses Can, and Do, Shift Gears

  3   Hotel Magnate Seeks Help to Save Publishing Bid                                                                                  Hotel King Seeks Help to Save Publishing Bid

  4   A plenteous supply: \"The United States is blessed to have a plentiful supply of oil and natural gas---we should be using it\"   A rich supply: \"The United States is blessed to have a plentiful supply of oil and natural gas---we should be using it\"

  5   In a sport full of corporate automatons, he will sit down and tell you what is on his mind, even if it is a lot.                 In a sport full of corporate zombies, he will sit down and tell you what is on his mind, even if it is a lot.

  6   The belligerents that can stop the war                                                                                           The fighters that can stop the war

  7   The Demise of the Public Library                                                                                                 The Death of the Public Library

  8   Gentlewomen of the Forbidden City: The Power, the Intrigue, the Clothes                                                          Ladies of the Forbidden City: The Power, the Intrigue, the Clothes
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Participants 

Participants were recruited using emails sent to a listserv of undergraduate students in a large research university in the United States. Prior to recruitment, the recruitment method and use of a survey study had been reviewed and approved by the University at Albany Institutional Review Board (IRB Study No. 22X113) and all participants had provided informed consent.

After completing the online survey, the participants were asked to forward invitations to their colleagues who may wish to participate, i.e., conduct snowball sampling. Qualtric.com was used to randomize the sentences shown to the participants**.** In a process called A/B random testing, ‎two variations of ‎the same element (‎A‎ ‎and ‎B‎‎), in this study two different pages, that differ only in ‎the variable being ‎tested, in this study one word in the sentences shown on the pages, are tested. ‎The words were tested for IE by showing 50% of the participants Page A and 50% Page B, with all participants viewing the words on a computer. The division of participants was performed computationally and cookies were placed on their computers so that they ‎would always return to the same page. The placement of cookies is important ‎in commercial ‎environments to ensure that users will not ‎notice the testing.

By balancing both known and unknown predictive factors, random assignment and title presentation reduced the risk of selection bias and allocation bias. Risk of bias was further decreased by withholding information that may have influenced the participants until after the experiment had been completed, i.e., the process of blinding. Overall, 5,532 participants were presented two variations of eight titles, as shown in the table below.

+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    |      | > **Count** | > **Table N %** |
+-----------------------+-----+--------------------+------+-------------+-----------------+
| > **Sentence Number** | > 1 | > Sentence Version | > 0  | > 332       | > 6.2%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 330       | > 6.2%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 2 | > Sentence Version | > 0  | > 344       | > 6.4%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 320       | > 6.0%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 3 | > Sentence Version | > 0  | > 331       | > 6.2%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 335       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 4 | > Sentence Version | > 0  | > 338       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 327       | > 6.1%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 5 | > Sentence Version | > 0  | > 324       | > 6.1%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 347       | > 6.5%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 6 | > Sentence Version | > 0  | > 339       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 335       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 7 | > Sentence Version | > 0  | > 339       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 337       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       | > 8 | > Sentence Version | > 0  | > 339       | > 6.3%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+
|                       |     |                    | > 1  | > 334       | > 6.2%          |
+-----------------------+-----+--------------------+------+-------------+-----------------+

### Procedure

Qualtric.com was used to administer the survey by randomly presenting the titles and collecting participant responses. After the participants had provided their informed consent (see S[ection 7.2](#_Introduction_and_informed)), they were asked to provide their demographic information (see [Section 7.3](#_Demographic_questions)). They were then randomly presented with a version of a title, either the original (control) or modified (treatment) version, and their level of IE assessed by asking questions related to the dimensions of IE. To measure perception, the participants were asked to rate the title for interest, value, readability, and other factors adopted from the UES \[@obrien2018\]; The full list of questions is in [Section 6.1](#_User_Engagement_Scale). To measure participation, the participants were asked whether they would like to read the entire article. To measure perseverance the participants were asked post-task questions to test whether they could recall the title, i.e., knowledge retention. For each title variant, three scores were computed: the perception score, the mean of the UES score; the participation rate, the percentage of participants who chose to read the full article; and the perseverance rate, the mean rate of retention (i.e., memory) of the title measured in terms of how many words on average were remembered.

## Results

The complete responses and results can be found on an [external spreadsheet of the raw data collected.](https://docs.google.com/spreadsheets/d/1WGS3S_zR7Z6uriPcjiomvfYmgoTpmgtD/edit?usp=sharing&ouid=102987810457035811283&rtpof=true&sd=true)

### H1: *Use of more engaging words ("sticky words") will positively influence the level of IE with the entire text as measured by participation, perception, and perseverance.* {#h1-use-of-more-engaging-words-sticky-words-will-positively-influence-the-level-of-ie-with-the-entire-text-as-measured-by-participation-perception-and-perseverance.-1 .unnumbered}

Modified sentences will have higher IE levels

  ---------------------------------------------------------------------------------------
  **Dimension**                   **Original**   **Modified**   **T**     **P**   **d**
  ------------------------------- -------------- -------------- --------- ------- -------
  **Perception (UES)**            3.17 (.79)     4.18 (.68)     -51.065   .000    .726

  **Participation (selection)**   .38 (.49)      .72 (.45)      -25.895   .000    .496

  **Perseverance (retention)**    3.09 (3.03)    3.44 (3.36)    -3.95     .000    3.20
  ---------------------------------------------------------------------------------------

Figure . Differences between IE Dimensions of Original and Modified Titles

The table and figure above show the differences in means between the original (n=2,686) and modified sentences (n=2,665) in the three IE dimensions. As hypothesized, the modified sentences had a higher mean perception score (4.1856 vs. 3.1733), mean selection rate (0.7152 vs. 0.3831), and mean retention rate (3.4353 vs. 3.0897). Independent sample t-tests for all three comparisons showed that the differences in means between the modified and original titles were significant, with high to moderate effect sizes, as shown in Table 4 and Figure 4. See [Section 7.3.1](#_Group_comparison) for the complete analysis.

However, examination of individual titles revealed that not all modified versions had significantly higher IE values for all three dimensions. Independent t-tests of the eight pairs of titles for the three IE dimensions indicated that while Titles 3, 4, 5, and 7 had **[significant differences for all three dimensions,]{.underline}** Titles 1, 2, 6, and 8 had **[significant differences in perception and participation but not in perseverance.]{.underline}** The tables and figures below show the results. [Section 7.3.2](#_Sentence_comparison) shows the complete analysis.

  -------------------------------------------------------------------------
  Title             Original   Modified   T          P           d
  ----------------- ---------- ---------- ---------- ----------- ----------
  1                 2.84       3.88       -18.420    \<.001      .729

  2                 3.51       4.33       -16.099    \<.001      .66

  3                 2.92       3.96       -20.042    \<.001      .67

  4                 3.40       4.33       -18.575    \<.001      .648

  5                 2.72       3.93       -21.930    \<.001      .72

  6                 3.20       4.32       -22.346    \<.001      .65

  7                 3.48       4.46       -20.077    \<.001      .63

  8                 3.27       4.26       -17.548    \<.001      .74
  -------------------------------------------------------------------------

Figure . Difference in UES scores between titles

  -------------------------------------------------------------------------
  Title             Original   Modified   T          P           d
  ----------------- ---------- ---------- ---------- ----------- ----------
  1                 .267       .667       -26.58     \<.001      .34

  2                 .55        .75        -16.67     \<.001      .36

  3                 .296       .679       -25.95     \<.001      .34

  4                 .485       .693       -18.45     \<.001      .36

  5                 .259       .360       -2.844     .005        .46

  6                 .374       .450       -2.01      .045        .49

  7                 .413       .504       -2.39      .017        .50

  8                 .404       .503       -2.585     .010        .50
  -------------------------------------------------------------------------

Figure . Difference in selection rate between titles

  -------------------------------------------------------------------------
  Title             Original   Modified   T          P           d
  ----------------- ---------- ---------- ---------- ----------- ----------
  1                 2.17       2.38       -.944      .346        2.9

  2                 2.14       1.85       1.828      .068        2.08

  3                 1.71       2.06       -2.285     .023        1.99

  4                 5.02       5.68       -2.060     .040        4.07

  5                 5.30       5.98       -2.389     .017        3.64

  6                 2.24       2.42       -1.143     .254        .649

  7                 2.92       3.37       -2.416     016         2.46

  8                 3.26       3.60       -1.437     .151        3.11
  -------------------------------------------------------------------------

Figure . Difference in retention between titles

# Dissertation discussion 

[For my doctoral research project, I have studied how digital text impact user experience (UX). My dissertation is titled "Sticky Words: A Computational Linguistics Approach to Assessment and Manipulation of Information Engagement". My main objective and expected research contribution was to develop predictive and prescriptive models for engaging text using natural language processing (NLP). Specifically, my dissertation includes three research projects that support each other. The first, titled "Conceptual Framework for Digital Information Engagement with Text" is an exploratory study on how users engage with digital information. I define information engagement based on a comprehensive literature review, and then demonstrate how engagement if influenced by changes in language through a series of large-scale online user surveys. In the second study, titled "]{.mark}[The READ Model: Representativeness, Ease-of-Use, Affect and Distribution as Predictors of Information Engagement", I developed a predictive model of textual engagement. Using advanced statistical analysis and regression models, I recognized and verified significant factors that predict which words will be more engaging to users -- better evaluated, selected, and retained. I also developed an original Python program that calculates words' predicted user engagement scores and chooses which synonyms to use. The third and final study, titled "Digital Information Manipulation and Assessment (DIMA)", is prescriptive application of my research. The predictive model was used to manipulate digital texts, and difference in responses was observed using large online AB testing. Results were significant and indicative to the applicable and valuable nature of this doctoral research.]{.mark}

This study explored new media engagement through the investigation of the effect of *sticky words*, words that are memorable, \"catchy,\" or otherwise compelling, on IE. Research shows that while most information consumed using new media technologies is quickly forgotten, use of sticky words can increase retention of information and improve IE. These messages can be systematically evaluated for and potentially developed for stickiness using semantic analysis, NLP techniques, and a rule-based approach.

This study proposed and validated a conceptual model of IE based on identification of its three dimensions. Validation of this model produced several significant results:

1.  IE is a driver for information use as operationalized as *participation* (retrieval or selection rate) and *perseverance* (retention and integration or memory).

2.  A significantly positive correlation exists among how information is evaluated; exchanged; employed; and integrated in terms of information effectiveness, adoption, and subsequent usage behavior.

3.  IE is an important research construct because it leads to desired outcomes in the form of positive affective, behavioral, and cognitive responses.

4.  IE is driven, if not determined, by how information is expressed, specifically by word choice

5.  IE is distinct from user engagement because it depends on only evaluation of the information itself, specifically of word choice independently of other user and system variables.

6.  Variations in the expression of the information (the phrasing used) impact perception as measured by user evaluation using the UES, participation as measured by information exchange or actions (e.g., information retrieval and user responses), and perseverance as measured by information retention and recall.

7.  Changes in IE impact perception, participation, and perseverance.

8.  Word choice is a significant factor such that synonym substitution can affect perception, participation, and perseverance, as well as knowledge retention.

These results suggest that by increasing the level of engagement with textual information, content providers can positively and significantly affect outcomes. Therefore, word choice is a factor that should be carefully considered in the production of textual content.

The main contribution of this study was demonstrating that text analysis and NLP can be used to systematically and automatically predict the IE level of a given word or phrase. Use of a program in Python specifically written for this study was able to accurately predict a word's IE level based on assessment of the four attributes of representativeness, ease-of-use, affect, and distribution. These four situational, stable, controllable, and easily measured attributes of IE were operationalized to develop the READ model, a computational predictive model that was found highly effective in predicting a word's IE levels in terms of perception score, selection rate, and retention rate. Use of the Python program and READ model was also found effective in identifying the more engaging word when more than one word was possible for a given expression.

Use of the model offers a plethora of opportunities for further research and application, in particular the potential of systematic, computational, and even automatic textual modification to influence UX, On a practical level, it can, for example, be used by governments to select textual information that encourages citizens to engage in healthful practices and avoid unhealthful ones. It can also be used in education to select engaging words for use in learning materials and in business settings to select words in marketing communications. Its potential to improve communication in these and other domains should be explored in further research.

Examining the characteristics of engaging messages allowed development of a measure of "stickiness" for quantitative evaluation of engaging language and systematically improvement of content strategy.

The results indicated that engaging words are not \"free-standing\"; when strategically placed, they impact their surrounding context and create a more engaging UX. This finding has great theoretical and practical implications for both academia and industry in terms of instructional design and marketing, respectively.

The overarching goal of the three research phases was to obtain results with which to develop a design approach and practical instrument to improve IE. Providing support that IE is driven by the information itself and is critical to successful information interactions has both practical applications, such as improving user participation, perception, perseverance, and other essential factors, as well as theoretical implications, such as the possibility that words can be manipulated to change cognition, whether in a positive or negative manner.

## Discussion

### Dimensions and measurements 

Based on the results, it is possible to validate the conceptual definition and dimensions proposed for IE. The results demonstrate that information engagement is a driver for information use, as operationalized in participation (retrieval or selection rate) and perseverance (retention and integration or memory). IE was observed to manifest through perception (evaluation of the information), participation (retrieval of the information and responses to it), and perseverance (adoption and diffusion of the information). The results revealed a significant positive correlation between how the information is evaluated, how it is exchanged and employed, and how it is integrated in terms of information effectiveness, adoption, and subsequent usage behavior. The findings indiated that IE is an important research construct, as it leads to desired outcomes in the form of positive affective, behavioral, and cognitive responses.

### Determinants

The results confirm that IE is driven, if not determined, by how the information is expressed, specifically the choice of words. They also demonstrate that IE is distinct from user UE because it depends on the information itself. Specifically, IE is dependent on word choice and independent of other user and system variables. Therefore, the findings support IBT, which emphasizes that the interaction, interpretation, and integration of information should be studied in relation to the information itself. As seen by the variance in the words IE scores, information-related behavior is determined by the phrasing used and not the system, task, or user demographics.

The results also revealed that variations in the expression of the information (the phrasing used) impacts the levels of perception, participation, and perseverance. Changes in IE level impact perception, measured by user evaluation using the UES; participation, measured by information exchange or actions (information retrieval and user responses); and perseverance, measured by information retention and recall.

### Some words are more engaging than others 

The significant differences and variations between words' means show that word choice is a significant factor in IE. Comparison between synonyms show synonym substitution can lead to key performance indicators, such as participation, perception, and knowledge retention. These results suggest that by increasing the level of engagement with textual information, content providers can positively and significantly affect outcomes. Therefore, word choice is a factor that should be carefully considered in the production of textual content.

## Discussion

**IE dimensions can be predicted systematically based on textual factors**

The main contribution of this study is demonstrating that text analysis and NLP can be used to predict the dimensions of IE systematically and automatically. This finding has great theoretical and practical implications for both academia and industry.

**A word's representativeness, ease-of-use, affect, and distribution scores can be used to predict its IE levels**

Representativeness, ease-of-use, affect, and distribution, four situational, stable, controllable, and easily measured attributes of engaging information, were operationalized to develop the READ model. This computational predictive model was found highly effective in predicting a word's IE levels in terms of perception score, selection rate, and retention rate.

**When there is more than one possible word to describe the same information, a word's representativeness, ease-of-use, affect, and distribution scores will predict whether a synonym of the word is more engaging**

Using the READ model and a Python program written specifically for this study, a reliable, novel computational tool was developed for identification of engaging words when more than one choice of word is possible. Use of the model offers a plethora of opportunities for further research and application, in particular the potential of systematic, computational, and even automatic textual modification to influence UX, On a practical level, it can, for example, be used by governments to select textual information that encourages their citizens to engage in healthful practices and avoid unhealthful ones. It can also be used in education to select engaging words to be used in learning materials, on in business settings to improve marketing communications. There are various options which should, and hopefully would, be explored in further research.

## Significance and future work  {#significance-and-future-work .unnumbered}

Gaining understanding of how and why information is retained is of fundamental interest to both academia and industry. Determining a method for effective communication is of paramount importance in many theoretical and applied domains, such as online marketing, education, and government initiatives. In the contexts of IT and New Media, engagement has been increasingly used as a possible framework to understand, measure, and optimize interactions with information in order to optimize UX. Improving IE in these domains requires examining the language used in the content presented. Language can thereby be considered a pragmatic toolkit helping to illuminate and influence human behavior. Words can be thought of as containers used ‎to carry information, with some more effective in conveying specific messages than others.

Focusing on the relationship between IE and the emerging fields of information design, content strategy, and computational linguistics, this study developed a novel approach to prediction and manipulation of IE. Specifically, a novel automatic method to systematically identify engaging words was developed and used to optimize sentences for engagement by replacing a word with its sticky equivalent.

Further work could use the findings of this study to develop an "IE classifier" for classification of words and quantitative measurement of IE. Its potential to quantify the level of "stickiness," or create an "engagement spectrum" based on the IE factors identified in this research holds great promise. This tool, as well as the original program and the READ model, can be applied to other types of media, including photos and videos. They can also be applied in domains other than academia or business, such as nonprofit organizations, where it can be used to select words that will increase IE with online petitioning.

From a methodological point of view, the main contribution was identifying the criteria for selecting powerful sticky words. The next logical step would be to derive reliable and reusable metrics and methodology for engagement. Using these metrics and methodology, a precise specification of engaging language could be developed for quantitative evaluation and operational formulation of "stickiness" and IE. Constructing an automatic method for effective communication will have major implications for users who desire to convey a message that will "stick," i.e., information that is engaging and memorable. Lastly, gaining better understanding of the characteristics of sticky language would allow for quantitative evaluation of engaging word choices for application in diverse domains that can then be extended to other domains. While it is not possible to develop a completely automated system for global application, i.e., across all domains, even partial advancement toward this goal would be useful to researchers and practitioners.

Significantly, this study identified and addressed two important gaps in the research regarding IE with textual data: how users react to information rather than why they become engaged with it and the best means of developing engaging information rather than simply measuring it. The findings suggest the effectiveness of a new systematic approach to optimizing engagement that includes the repackaging of distinct content. The ultimate research contribution is identification of criteria and metrics for selecting powerful and engaging, i.e., sticky, words, and development of a novel method for manipulating and measuring IE. Use of this method will aid in the larger task of understanding, enabling, and optimizing IE.

[My current research projects focus on the relationship between content strategy and UX, specifically how user engagement is driven and fostered by digital text. I also study how natural language processing (NLP) and computational linguistics techniques can be used to systematically improve UX, information behavior, retention, and growth.]{.mark}

**Limitations**

This study faced several limitations that may have affected the results. The primary limitation was that only one population, undergraduate students at one university, was examined. Investigation of other populations may have yielded very different results and should therefore be conducted in future studies. Another limitation was the use of snowball sampling as the method of recruitment. Like any nonrandom sampling method, snowball sampling does not ensure representation, and it also has a particular susceptibility to sampling bias. Because the participants are selected by individuals who have already been selected, they are likely to share certain characteristics or traits, further increasing the risk of nonrepresentation. To overcome this limitation, the findings of this study should be substantiated or refuted by conducting studies using alternative or complementing ‎‎approaches and techniques. A third limitation was the difficulty of substituting words for more sticky words in an academic text without changing the overall meaning, intention, and/or tone. A final limitation that the text examined was only academic text. Investigation of text in other domains may have yielded different results.

## Discussion 

**Substituting words with more engaging synonyms will positively influence the level of IE with the entire text**

The main finding of this study is that replacing a word with a more engaging synonym, i.e., with a sticky word, will increase IE with the entire text. Overall, the modified sentences had significantly higher participation scores, selection rates, and retention rates than their original versions. When observed individually, four of the titles had significantly higher scores on all three dimensions and four had significantly higher participation scores and selection rates but not retention rates. These findings indicate that synonym substitution using sticky words is an effective way to improve IE with digital texts.

**It is possible to computationally predict which words will be sticky words**

Using the READ model to predict more engaging synonyms resulted in significant differences between responses to texts containing sticky words and those that did not. This shows that using scores for representativeness, ease-of-use, affect and distribution can lead to prediction and prescription of words that will be more engaging, leading to better IE.

**Results vary based on other factors**

While computing systems are deterministic, human behavior is much more complex. User engagement is not the product of a single process; rather, it reflects the interaction of diverse specialized mechanisms, including emotional and rational processes. Research shows that users are more likely to be engaged when decision-making is controlled by emotional processes, which are generally automatic, affective, and heuristic-based. By appealing to their emotions, desires, and aspirations, the use of sticky words can be strategically implemented to improve UX and increase IE.

However, as use of sticky words has not been definitively proven to increase IE, other factors, such as topic, context, and user preferences, may also play significant roles. Moreover, factors other than individual word selection may affect IE with a given sentence or text. In linguistics, two types of expression may be used for one concept or meaning, an *analytic expression* or a *synthetic expression* (Zhou, 2012). The former is use of a phrase or sentence to express a meaning or concept while the latter is use of one word to do so. If two means of expressing the same meaning are possible, the synthetic expression is preferred because it adheres to the *economy principle*, the conveyance of the most information with the least effort, which decreases the amount of cognitive processing necessary for understanding.

Phrases as well as words may decrease cognitive load, particularly *collocations*, the juxtaposition of a word with another word or words with which it always or almost always appears, e.g., "land a deal" or "forgive a debt" (Basel, 2019). By saving cognitive energy and time by conveying more information with less effort, the use of collocations may increase IE with the sentences in which they appear/ Another linguistic phenomenon that likewise saves cognitive effort is the use of common and easily understood metaphors, e.g., "bear market" or "raining cats and dogs" (Lakoff & Mark, 1980). In terms of morphology, the manipulation of voice, which is often used to affect perception, is likely to also affect IE. For example, politicians frequently use the passive voice in the sentence "Mistakes were made" instead of using the active voice in the sentence "I made a mistake" to escape blame while not formally lying. Doing so may not only maintain confidence in the politician but improve IE with any textual information provided by the politicians. The possibility that factors besides simply one word affect IE indicates that the whole, i.e., the sentence, is greater than the sum of its parts, i.e., the individual words.

**Significance and future work**

The findings ‎are limited and preliminary. While not sufficient to validate causation, they are sufficiently robust to warrant further ‎investigation as part of an exploratory longitudinal research project. Such a project would provide additional data with which to further develop the proposed system and then use it to systematically identify and develop engaging content. It would be based on a computational approach that optimizes content for engagement by replacing words with their stickier equivalents, that is, words that are emotionally charged, familiar, and easy to read.

Ultimately, the findings could be applied to build a "sticky classifier." As mentioned previously, a classifier is a set of factors that are used to label a word for its level of engagement. The primary obstacle to doing so is the lack of an annotated dataset for sticky words. As a next step, HITs Amazon Mechanical Turk be used to annotate a large compilation of academic titles for stickiness that could then use to model a sticky classifier. While this model would be domain-specific in that it would be developed to classify titles in text, further refinement could allow for extrapolation to other domains.

For this purpose, use of an unsupervised machine-learning approach, specifically feature learning, which does not require an annotated dataset, may be appropriate. However, development of an unsupervised machine-learning model requires an immense amount of data. Identification of a large dataset that contains many examples of words proven to be sticky across domains could be used to investigate feature learning, the transformation of raw data into input e.g., academic titles into a representation, or a feature set that can be effectively exploited in machine-learning tasks. If this process can be used to automatically identify features important to stickiness---familiarity, representativeness, ease of use, and emotionality---a model based on sticky features across domains could be developed. The challenges to this approach are the need to perform feature selection, the separation of the features related to stickiness from a large feature set containing numerous types of other features, and the need to validate the model, which poses difficulties similar to that of obtaining an annotated dataset. Moreover, after building the model, a way to quantitatively test its effectiveness, which would require annotators or domain experts, must be developed.

# References {#references .unnumbered}

{Abbas, \"Structures for organizing knowledge: exploring taxonomies, ontologies, and other schemas\", 2010}

{Abraham et al., \"Evaluating the effectiveness of learner controlled information security training\", 2019}

{Akdeniz et al., \"Effectiveness of marketing cues on consumer perceptions of quality: The moderating roles of brand reputation and third-party information\", 2013}

{Alter et al., \"Easy on the mind, easy on the wallet: The roles of familiarity and processing fluency in valuation judgments\", 2008}

{Appleton et al., \"Student engagement with school: Critical conceptual and methodological issues of the construct\", 2008}

{Aranyi et al., \"Modeling user experience with news websites\", 2015}

{Arapakis et al., \"Understanding within-content engagement through pattern analysis of mouse gestures\", 2014}

{Arapakis et al., \"User engagement in online news: Under the scope of sentiment, interest, affect, and gaze\", 2014}

{Arapakis et al., \"On the feasibility of predicting popular news at cold start\", 2017}

{Attfield et al., \"Towards a science of user engagement (position paper)\", 2011}

{Baccianella et al., \"Sentiwordnet 3.0: an enhanced lexical resource for sentiment analysis and opinion mining.\", 2010}

{Bahry et al., \"Website evaluation measures, website user engagement and website credibility for Municipal website\", 2015}

{Bardus et al., \"A review and content analysis of engagement, functionality, aesthetics, information quality, and change techniques in the most popular commercial apps for weight management\", 2016}

{Barthel, \"5 key takeaways about the State of the News Media in 2016\", 2016}

{Batra et al., \"Affective Responses Mediating Acceptance of Advertising\", 1986}

{Begany et al., \"An open health data engagement ecosystem model: Are facilitators the key to open data success?\", 2017}

{Berger et al., \"What Makes Online Content Viral?\", 2012}

{Bialik et al., \"Key trends in social and digital news media\", 2017}

{Bird et al., \"Natural Language Processing with Python\", 2019}

{Bloch et al., \"Exploring the origins of enduring product involvement\", 2009}

{Blythe et al., \"The Semantics of Fun: Differentiating Enjoyable Eeperiences\", 2003}

{Blythe et al., \"Funology From Usability to Enjoyment\", 2005}

{Bomia et al., \"The Impact of Teaching Strategies on Intrinsic Motivation\", 1997}

{Boyle et al., \"Engagement in digital entertainment games: A systematic review\", 2012}

{Brodie et al., \"Customer engagement: Conceptual domain, fundamental propositions, and implications for research\", 2011a}

{Brodie et al., \"Customer Engagement: Conceptual Domain, Fundamental Propositions, and Implications for Research\", 2011}

{Brodie et al., \"Consumer engagement in a virtual brand community: An exploratory analysis\", 2013}

{Bruns, \"Blogs, Wikipedia, Second Life, and Beyond: From Production to Produsage\", 2008}

{Brysbaert et al., \"The Word Frequency Effect: A Review of Recent Developments and Implications for the Choice of Frequency Estimates in German\", 2011}

{Burton-Jones et al., \"Toward a Deeper Understanding of System Usage in Organizations: A Multilevel Perspective\", 2007}

{Cairns, \"Engagement in Digital Games\", 2016}

{Chan et al., \"User engagement in e-government systems implementation: A comparative case study of two Singaporean e-government initiatives\", 2008}

{Chapman et al., \"Engagement in multimedia training systems\", 1999}

{Chapman, \"Alternative approaches to assessing student engagement rates\", 2003}

{Chen et al., \"The effects of information overload on consumers' subjective state towards buying decision in the internet shopping environment\", 2009}

{Cheng et al., \"You Had Me at Hello: How Phrasing Affects Memorability\", 2012}

{Cole, \"Using Wiki technology to support student engagement: Lessons from the trenches\", 2009}

{Commuri et al., \"An enlargement of the notion of consumer vulnerability\", 2008}

{Czerlinski et al., \"How good are simple heuristics?\", 1999}

{DeLone et al., \"Information systems success: The quest for the dependent variable\", 1992}

{DeLone et al., \"The DeLone and McLean model of information systems success: A ten-year update\", 2003}

{deNoyelles et al., \"Using Word Clouds in Online Discussions to Support Critical Thinking and Engagement\", 2015}

{DePaula et al., \"Information strategies and affective reactions: How citizens interact with government social media content\", 2018}

{Dewey, \"Experience and education\", 1998}

{Dhanesh, \"Putting engagement in its PRoper place: State of the field, definition and model of engagement in public relations\", 2017}

{Dincelli et al., \"Choose your own training adventure: designing a gamified SETA artefact for improving information security and privacy through interactive storytelling\", 2020}

{Dolan et al., \"Social media engagement behaviour: a uses and gratifications perspective\", 2016}

{Dumas et al., \"Examining political mobilization of online communities through e-petitioning behavior in We the People\", 2015}

{Dvir, \"The Influence Of Gender On Consumer‎ behavior And Decision Making In Online‎ and Mobile Learning‎ environments\", 2015}

{Dvir, \"Mitigating challenges of open government data\", 2017}

{Dvir, \"Sticky words: Evaluation and optimization of information interactions based on linguistic analysis\", 2018}

{Dvir et al., \"When less is more: empirical study of the relation between consumer behavior and information provision on commercial landing pages\", 2018}

{Dvir et al., \"Systematic improvement of user engagement with academic titles using computational linguistics\", 2019}

{Eisenstein et al., \"Turning Lectures into Comic Books Using Linguistically Salient Gestures\", 2007}

{\"Engagement\", 2020}

{Eppler et al., \"The concept of information overload: A review of literature from organization science, accounting, marketing, MIS, and related disciplines\", 2004}

{Eppler, \"Managing information quality: Increasing the value of information in knowledge-intensive products and processes\", 2006}

{Facebook.com, \"Likes, Reach & Engagement\", 2016}

{Feng et al., \"Content marketing: A review of academic literature and future research directions\", 2015}

{Finucane et al., \"The affect heuristic in judgments of risks and benefits\", 2000}

{Fredricks et al., \"School engagement: Potential of the concept, state of the evidence\", 2004}

{Frick, \"Return on Engagement: Content, Strategy, and Design Techniques for Digital Marketing\", 2010}

{Frické, \"The knowledge pyramid: a critique of the DIKW hierarchy\", 2009}

{Gafni et al., \"How content volume on landing pages influences consumer ‎‎behavior: empirical evidence\", 2018}

{Gigerenzer et al., \"Reasoning the fast and frugal way: models of bounded rationality.\", 1996}

{Gigerenzer et al., \"Fast and frugal heuristics: The adaptive toolbox\", 1999}

{Gill, \"Informing Science Volume One: Concepts and Systems\", 2015}

{Gofman, \"Consumer driven multivariate landing page optimization: overview, issues and outlook\", 2007}

{Gofman et al., \"Integrating science into web design: consumer‐driven web site optimization\", 2009}

{Google, \"The Engagement Project: The VICE Guide to Engagement\", 2013}

{Grimmelikhuijsen et al., \"The Effect of Transparency on Trust in Government: A Cross-National Comparative Experiment\", 2013}

{Guerini et al., \"Do linguistic style and readability of scientific abstracts affect their virality?\", 2012}

{Guo et al., \"How video production affects student engagement: an empirical study of MOOC videos\", 2014}

{Gutman, \"A Means-End Chain Model Based on Consumer Categorization Processes\", 1982}

{Hagen et al., \"E-petition popularity: Do linguistic and semantic factors matter?\", 2016}

{Hart et al., \"Evaluating User Engagement Theory\", 2012}

{Hassenzahl et al., \"User experience - a research agenda\", 2006}

{Hearst, \"Untangling Text Data Mining\", 1999}

{Horrigan, \"How People Approach Facts and Information\", 2017}

{Huang et al., \"Sharing is caring: Social support provision and companionship activities in healthcare virtual support communities\", 2019}

{Im et al., \"ICT as a buffer to change: A case study of the Seoul Metropolitan Government's Dasan Call Center\", 2013}

{Imlawi, \"Health Website Success: User Engagement in Health-Related Websites\", 2017}

{ISO 9241, \"Ergonomics of human-system interaction: Part 210: Human-centred design for interactive systems\", 2019}

{Jacques et al., \"Engagement as a Design Concept for Multimedia.\", 1995}

{Jacques, \"The nature of engagement and its role in hypermedia evaluation and design.\", 1996}

{Jarvenpaa et al., \"Consumer Trust in an Internet Store: A Cross-Cultural Validation\", 2006}

{Jennings, \"Theory and models for creating engaging and immersive ecommerce websites\", 2000}

{Jiang et al., \"Social media engagement as an evaluation barometer: Insights from communication executives\", 2016}

{Johns, \"The essential impact of context on organizational behavior\", 2006}

{Johnson, \"Gender differences in e-learning: Communication, social presence, and learning outcomes\", 2011}

{Johnston et al., \"The handbook of communication engagement\", 2018}

{Kahneman et al., \"Subjective probability: A judgment of representativeness\", 1972}

{Kahneman et al., \"Prospect Theory: An Analysis of Decision under Risk\", 1979}

{Kahneman et al., \"Representativeness Revisited: Attribute Substitution in Intuitive Judgment\", 2002}

{Kearsley et al., \"Engagement Theory: A Framework for Technology-Based Teaching and Learning\", 1998}

{Kelley, \"Attribution theory in social psychology.\", 1967}

{Kodagoda et al., \"Using Machine Learning to Infer Reasoning Provenance From User Interaction Log Data: Based on the Data/Frame Theory of Sensemaking\", 2016}

{Koehler et al., \"What do saliency models predict?\", 2014}

{Kornell et al., \"The Ease-of-Processing Heuristic and the Stability Bias: Dissociating Memory, Memory Beliefs, and Memory Judgments\", 2011}

{Kostkova, \"User Engagement with Digital Health Technologies\", 2016}

{Koufaris, \"Applying the technology acceptance model and flow theory to online consumer behavior\", 2002}

{Lagun et al., \"Understanding User Attention and Engagement in Online News Reading\", 2016}

{Lalmas et al., \"Measuring user engagement\", 2014}

{Laurel, \"Computers as theatre\", 2014}

{Lee et al., \"A Trust Model for Consumer Internet Shopping\", 2001}

{Legg et al., \"Do You Want the Good News or the Bad News First? The Nature and Consequences of News Order Preferences\", 2014}

{Lehmann et al., \"Models of user engagement\", 2012b}

{Li et al., \"A faceted approach to conceptualizing tasks in information seeking\", 2008}

{Lindgaard et al., \"Attention web designers: You have 50 milliseconds to make a good first impression!\", 2006}

{Liu, \"Sentiment analysis and opinion mining\", 2012}

{Lopez et al., \"NOMIT: Automatic Titling by Nominalizing\", 2012}

{Loureiro et al., \"Sentiment Analysis of News Titles\", 2011}

{Ma et al., \"Gender differences of knowledge sharing in online learning environment\", 2011}

{Malthouse et al., \"The Effects of Media Context Experiences On Advertising Effectiveness\", 2007}

{Martin et al., \"Digital Transformations? Gendering the End User in Digital Government Policy\", 2016}

{McCay-Peet et al., \"A Model of Social Media Engagement: User Profiles, Gratifications, and Experiences\", 2016}

{Meece et al., \"Students' goal orientations and cognitive engagement in classroom activities.\", 1988}

{Mekler et al., \"A Systematic Review of Quantitative Studies on the Enjoyment of Digital Entertainment Games\", 2014}

{Miles et al., \"Qualitative data analysis: A methods sourcebook\", 2014}

{Miller, \"WordNet: a lexical database for English\", 1995}

{Mishra et al., \"IS Use\", 2017}

{Mitchell et al., \"How Americans Encounter, Recall and Act Upon Digital News\", 2017c}

{Mitchelstein et al., \"Online news consumption research: An assessment of past work and an agenda for the future\", 2010}

{Mollen et al., \"Engagement, telepresence and interactivity in online consumer experience: Reconciling scholastic and managerial perspectives\", 2010d}

{Nardi, \"Context and consciousness: activity theory and human-computer interaction\", 1996}

{Navajas, \"New Technologies and Civic Engagement; Personalization and the Future of News (Ch. 12)\", 2014}

{Nevo et al., \"A temporally situated self-agency theory of information technology reinvention\", 2016}

{Newmann, \"Student engagement and achievement in American secondary schools.\", 1992}

{Nielsen, \"Ten usability heuristics\", 2005}

{Nielsen, \"World's Best Headlines: BBC News\", 2009}

{Nielsen, \"Legibility, Readability, and Comprehension: Making Users Read Your Words\", 2015}

{Norman, \"The design of everyday things\", 2013}

{O'Brien et al., \"What is user engagement? A conceptual framework for defining user engagement with technology\", 2008}

{O'Brien et al., \"The development and evaluation of a survey to measure user engagement\", 2010}

{O'Brien, \"The Influence of Hedonic and Utilitarian Motivations on User Engagement: The Case of Online Shopping Experiences\", 2010}

{O'Brien, \"Exploring user engagement in online news interactions\", 2011}

{O'Brien et al., \"What motivates the online news browser? News item selection in a social information seeking scenario\", 2014}

{O'Brien et al., \"Investigating the role of user engagement in digital reading environments\", 2016e}

{O'Brien, \"Translating Theory into Methodological Practice\", 2016}

{O'Brien et al., \"What makes online news interesting? Personal and situational interest and the effect on behavioral intentions\", 2016}

{O'Brien et al., \"Why engagement matters: Cross-disciplinary perspectives of user engagement in digital media\", 2016}

{O'Brien, \"Antecedents and learning outcomes of online news engagement\", 2017}

{O'Brien et al., \"Learning From the News: The Role of Topic, Multimedia and Interest in Knowledge Retention\", 2017}

{O'Brien et al., \"A practical approach to measuring user engagement with the refined user engagement scale (UES) and new UES short form\", 2018}

{O'Brien et al., \"Modeling Antecedents of User Engagement\", 2018}

{O'Brien et al., \"An empirical study of interest, task complexity, and search behaviour on user engagement\", 2020}

{Oestreicher-Singer et al., \"Content or Community? A Digital Business Strategy for Content Providers in the Social Age\", 2012}

{Oh et al., \"User Engagement with Interactive Media: A Communication Perspective\", 2016}

{O'Reilly, \"Government as a platform\", 2010}

{Overbeeke et al., \"Let's Make Things Engaging\", 2003}

{\"Perception\", 2021}

{Perski et al., \"Conceptualising engagement with digital behaviour change interventions: a systematic review using principles from critical interpretive synthesis\", 2017}

{Plummer et al., \"Measures of engagement\", 2006}

{Princeton University, \"About WordNet\", 2018}

{Rainie et al., \"Information Searches That Solve Problems\", 2007}

{Reis et al., \"Breaking the News: First Impressions Matter on Online News\", 2015}

{Ritchie et al., \"Making Information Memorable: Enhanced Knowledge Retention and Recall Through the Elaboration Process\", 1996}

{Rock Health, \"Digital Health Consumer Adoption: 2015\", 2015}

{Rowley, \"Understanding digital content marketing\", 2008}

{Savin, \"Word‐Frequency Effect and Errors in the Perception of Speech\", 1963}

{Schmidt et al., \"Anatomy of news consumption on Facebook\", 2017}

{Shahaf et al., \"Inside Jokes: Identifying Humorous Cartoon Captions\", 2015}

{Sharon, \"Measuring user engagement\", 2018}

{Shneiderman et al., \"Designing the user interface: strategies for effective human-computer interaction\", 2016}

{Singh et al., \"Customer Engagement: New Key Metric of Marketing\", 2010}

{Smith, \"Record shares of Americans now own smartphones, have home broadband\", 2017}

{So et al., \"Student perceptions of collaborative learning, social presence and satisfaction in a blended learning environment: Relationships and critical factors\", 2008}

{Soto-Acosta et al., \"The effect of information overload and disorganisation on intention to purchase online: The role of perceived risk and internet experience\", 2014}

{Speer et al., \"LuminosoInsight/wordfreq: v2.2\", 2018}

{Stewart, \"Conceptualising engagement\", 2009}

{Stockdale et al., \"An interpretive approach to evaluating information systems: A content, context, process framework\", 2006}

{Stocking, \"Digital News Fact Sheet\", 2017}

{Stroud et al., \"Engaging audiences via online news sites\", 2015}

{Sutcliffe, \"Designing for User Experience and Engagement\", 2016}

{Sutton et al., \"COVID-19: Retransmission of official communications in an emerging pandemic\", 2020}

{Szabo et al., \"Predicting the popularity of online content\", 2008}

{Turney et al., \"The natural selection of words: Finding the features of fitness\", 2019}

{Tversky et al., \"Judgment under uncertainty: Heuristics and biases\", 1974}

{Tversky et al., \"The Framing of Decisions and the Psychology of Choice\", 1981}

{Tversky et al., \"Advances in prospect theory: Cumulative representation of uncertainty\", 1992}

{Uskul et al., \"When message-frame fits salient cultural-frame, messages feel more persuasive\", 2010}

{Vakkari, \"Task-based information searching\", 2003}

{Venkatesh et al., \"Technology acceptance model 3 and a research agenda on interventions\", 2008}

{Venkatesh et al., \"Extending the two-stage information systems continuance model: incorporating UTAUT predictors and the role of context: Context, expectations and IS continuance\", 2011}

{Webster et al., \"Analyzing the Past to Prepare for the Future: Writing A Literature Review\", 2002}

{Weinmann et al., \"Digital Nudging\", 2016}

{Wells et al., \"What signal are you sending? How website quality influences perceptions of product quality and purchase intentions\", 2011}

{Westman, \"What motivates the online news browser? News item selection in a social information seeking scenario\", 2013f}

{Wiebe et al., \"Measuring engagement in video game-based environments: Investigation of the User Engagement Scale\", 2014}

{Willett et al., \"Untangling search task complexity and difficulty in the context of interactive information retrieval studies\", 2014}

{Wilson, \"On user studies and information needs\", 1981}

{Wilson, \"Information behaviour: An interdisciplinary perspective\", 1997}

{Wilson, \"Human information behavior\", 2000}

{Wilson, \"Fifty years of information behavior research\", 2010}

{Xu et al., \"Effects of Symbol Sets and Needs Gratifications on Audience Engagement: Contextualizing Police Social Media Communication\", 2019}

{Zheng et al., \"Building brand loyalty through user engagement in online brand communities in social networking sites\", 2015}

{Zins, \"Conceptual approaches for defining data, information, and knowledge\", 2007}

[^1]: asdsadsdas

[^2]:

[^3]: https://wordnet.princeton.edu/

[^4]: https://github.com/shivam5992/textstat

[^5]: https://github.com/LuminosoInsight/exquisite-corpus

[^6]: https://www.allsides.com/media-bias/media-bias-chart
