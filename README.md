# universe-GAN-research

# 1. Abstract:

Despite the breakthroughs in accuracy and speed of current Generative adversarial neural networks (GANs) we mostly focused on generating human faces, abstract art, super resolution and many other applications. What we did not yet try or put an emphasis on is: nebulae and celestial bodies generation using generative adversarial neural networks.

The fact that we did not try yet to use the power of GANs in the field of astronomy is mostly because we do not have large datasets of real data to work with (in this case images). If we are taking about celestial bodies, we only have a few real images of planets at our disposal (which are from our own solar system, which means a very limited amount), provided by NASA's Hubble Telescope and other telescopes.

In this paper we are focusing on using existent GAN algorithms, for image generation, for image upscaling and enhancement, combining these kinds of GAN algorithms in order to get a good end result, optimization of such GANs and  most important: Data collection and augmentation.

The generation of such images could have various applications in the astronomy field such as the visual enhancement of planetary and nebulae imagery (we would use the generated data as a new dataset to train an image enhancement algorithm) ,  planet detection and many others.

# 2. Classification:

1. AMS:   68T07	Artificial neural networks and deep learning
2. ACM: 
    - I. Computing Methodologies
    - I.4 IMAGE PROCESSING AND COMPUTER VISION
    - I.4.0 General

# 3. Introduction:

The generation of abstract astral objects and nebulae would be relevant because we lack data in order to train ML and DL algorithms for recognition and other purposes. So here come GANs into play to generate high quality images of planets, moons, stars, etc. that do not exist.

We found a lot of papers that generate galaxies in order to be used for galaxies shape classification.

### Related work:

The datasets used for the training of these GANs are collected from public websites and are not found in a dataset, because very few dataset on space imagery exist at the time of writing this.

A lot of other work is only related to the Galaxy generation, any nearly none focus on celestial bodies generation and nebula generations. This is mostly because the lack of data (only having very few real images of planets, and the ones we do have are from our own solar system- so we do not have diversity)

Articles related to Galaxy generation

- "Interpreting Galaxy Deblender GAN from the Discriminator's Perspective" ([https://www.researchgate.net/publication/338688374_Interpreting_Galaxy_Deblender_GAN_from_the_Discriminator's_Perspective](https://www.researchgate.net/publication/338688374_Interpreting_Galaxy_Deblender_GAN_from_the_Discriminator's_Perspective))
- "Galaxy Image Simulation Using Progressive GANs" ([https://www.adass2019.nl/wp-content/uploads/adass-pdf/Poster170.pdf](https://www.adass2019.nl/wp-content/uploads/adass-pdf/Poster170.pdf))

### Original contribution:

Algorithms:

We use well known GAN algorithms like: StyleGan2 and a light-weight version of StyleGan2, post processing done with a custom GAN used for resolution and image enhancement (the original contribution here would be the entanglement of the 2 algorithms and techniques)

Data:

Nebulae - Using real long exposure high quality images of nebulae, using DSLR cameras, dataset is around 1600 images (fetched from Wikimedia Commons)

Celestial bodies - Small dataset of about 300 images (60% fake art images and 40% real images of celestial bodies from our own solar system)

Research questions:

1. Can we generate accurate celestial body data in order to be used for future trainings, and even for other applications ?
2. How can we optimize a generative adversarial neural network to work with abstract images like images of galaxies, nebulas and celestial bodies [12]
3. How can we use deep learning to generate pictures non existing galaxies, nebulas and celestial bodies using real and fictive data

Overall presentation:

1. Right now, the research of generative adversarial neural networks on abstract data such as galaxies, nebulas and celestial bodies is rather slim and we want to find a way to improve and build upon existent GAN algorithms and techniques in order to get better results
2. A contribution in the deep learning GAN would also help in the digital art field
3. We could also find usage in prediction and enhancement of telescope imagery of galaxies, nebulas and celestial bodies in the future, in the astronomy research area
4. We could use generated celestial bodies or galaxies to as input data to help classify existing  celestial bodies or galaxies using different classification algorithms and techniques [13]

# 4.Modelling the experimental part:

### DATA:

- Images used for nebulae generation:
    - Using high resolution nebulae images captured by multiple people, using special telescopes and DSLR cameras, each taking multiple hours of long exposure and postprocess the images using software like: DeepSkyStalker and Photoshop
    - We use a dataset of around 1600 images fetched from  Wikimedia Commons
- Images used for celestial bodies generation:
    - Using around 300 images in total (small dataset) gathered by me, ~60% of images representing fictive images of planets made by artists and published on artwork websites, such as DeviantArt and Flickr; and ~40% representing real images of planets in our solar system taken by Nasa and published online.
    - Did not manage to find a good dataset of planets that can be used in the purpose  of our project, so the original contribution also includes building a dataset of planet imagery
- All the images are cropped in a 1:1 aspect ratio before being used for training

## Experiments:

- As experiments we need to use different GAN generation algorithms and techniques (2 good ones that can be used would be StyleGAN2 and lightweight GAN), get the results and postprocess them (increase resolution and color tweak)
- After the postprocessing we compare them with real images of nebulae and see if we consider that our generated image could might as well look like a real one or not
- Unfortunately, there are not so many generated images of nebulae and celestial bodies to compare our own with, so we need to use the little real data that we have and draw conclusions on our experiment

## Comparison:

- Generate pictures using existing GANs and compare the generated images with the ones we generated using GANs and applying upscaling and image improvements
- We can visually compare the results of the 2 methods and see if we can notice any improvement

### - Case study:

### Nebula generation:

- we used about 1600 real long exposure post processed images
- trained a light weight GAN for 600 epochs / 5000 epochs

![generated-images-0614.png](https://i.postimg.cc/XvSSCBwK/generated-images-0614.png)

- we can observe that even with only 600 epochs we have realistic looking nebulas (gathering high quality images might have helped a lot)

![Generated using GAN](https://i.postimg.cc/QdRsJyrT/output.jpg)

Generated using GAN

![Real nebula image](https://i.postimg.cc/TYNTpP7Q/0076.jpg)

Real nebula image

![Nebula after ESRGAN upscaling](https://i.postimg.cc/NMxcYG26/output-out.jpg)

Nebula after ESRGAN upscaling

### Celestial body generation:

- we used about 300 fake and real images of planets found on various websites such as deviant art (for fake images) and NASA (for real celestial bodies images)
- trained a style light GAN for 6000 epochs / 150000 epochs
- the light weight GAN also generates additional images from the initial ones by modifying picture brightness, position and other parameters

![6.jpg](https://i.postimg.cc/X7YVj58p/6.jpg)

- at about 6000 epochs the round shapes are starting to appear and colors look more realistic

![Generated using light weight style GAN](https://i.postimg.cc/t41pPH8b/6-crop-auto-x2.jpg)

Generated using light weight style GAN

![Real image of Pluto taken by NASA's New Horizons spacecraft in 2015 ](https://i.postimg.cc/0QnLFthZ/Untitled.png)

Real image of Pluto taken by NASA's New Horizons spacecraft in 2015 

### ESRGAN for upscaling

After finishing with planet generation we are applying ESRGAN for image enhancement 

Using upscaling to smoothen and change the resolution of the output image

![Planet-ESRGAN(1).PNG](https://i.postimg.cc/BbQGvW2d/Planet-ESRGAN-1-PNG.png)

![Second example](https://i.postimg.cc/C5PpBvNd/Capture-PNG.png)

Second example

# 5.Results and conclusions:

After training for many epochs and optimizing the resulted images we have results that start to resemble celestial bodies. Some of the images that we got present some exoplanet features, we can see that by the amount of water and land on the surface of the resulted celestial body. This happens because of the large amount of exoplanet artworks that our fictional dataset contains.

Some of the resulted images do not present all the celestial body features that we would want them to present, a cause of this is the lack of data, but this could see future improvements as we extract good resulted images and we feed the neural network with the new ones, so as we generate more accurate images we can re train our model and improve the results.

To respond to the research questions we formulated earlier, we can say that, for the question: “How can we use deep learning to generate pictures non existing galaxies, nebulas and celestial bodies using real and fictive data”, we can use as the answer the 2 trained models and the outcomes of this technique. 

We can conclude that we can generate celestial body imagery in order to be used for future trainings according to question number 1. So far we can not really tell how accurate the output is because the lack of data, but we can definitely say that the data that we produce is good enough to be used as future training data.

In order to generate abstract nebulae images we are using StyleGan2 which seems to perform really good on abstract images such as nebulae.

# Bibliography:

1. "Anomaly detection in Hyper Suprime-Cam galaxy images with generative adversarial networks" ([https://arxiv.org/abs/2105.02434](https://arxiv.org/abs/2105.02434))
2. "Generative Adversarial Nets" - University of Montreal

([https://arxiv.org/pdf/1406.2661.pdf](https://arxiv.org/pdf/1406.2661.pdf))

1. "A Neural Algorithm of Artistic Style"

([https://arxiv.org/pdf/1508.06576.pdf](https://arxiv.org/pdf/1508.06576.pdf))

1. "Hubble Astronomers Assemble Wide View of the Evolving Universe" - NASA

([https://www.nasa.gov/feature/goddard/2019/hubble-astronomers-assemble-wide-view-of-the-evolving-universe](https://www.nasa.gov/feature/goddard/2019/hubble-astronomers-assemble-wide-view-of-the-evolving-universe))

1. "AI and Machine Learning for Coders A Programmers Guide to Artificial Intelligence" - O'Reilly (Book) ([https://www.oreilly.com/library/view/ai-and-machine/9781492078180/](https://www.oreilly.com/library/view/ai-and-machine/9781492078180/))
2. "Generative Adversarial Networks" - Hands on machine learning O'Reilly (Book)

([https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632](https://www.oreilly.com/library/view/hands-on-machine-learning/9781492032632/))

1. "Artificial Intelligence A Modern Approach, 3rd Edition" - Stuart J. Russell, Peter Norvig ([https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597](https://www.amazon.com/Artificial-Intelligence-Modern-Approach-3rd/dp/0136042597))
2.  "Forging new worlds: high-resolution synthetic galaxies with
chained generative adversarial networks" ([https://arxiv.org/pdf/1811.03081.pdf](https://arxiv.org/pdf/1811.03081.pdf))
3. "Galaxy Image Classification Based on Citizen Science Data: A Comparative Study" ([https://ieeexplore.ieee.org/abstract/document/9025242](https://ieeexplore.ieee.org/abstract/document/9025242))
4. "Interpreting Galaxy Deblender GAN from the Discriminator's Perspective" ([https://www.researchgate.net/publication/338688374_Interpreting_Galaxy_Deblender_GAN_from_the_Discriminator's_Perspective](https://www.researchgate.net/publication/338688374_Interpreting_Galaxy_Deblender_GAN_from_the_Discriminator's_Perspective))
5. "Generative Adversarial Networks recover features in astrophysical images of galaxies beyond the deconvolution limit" ([https://arxiv.org/abs/1702.00403](https://arxiv.org/abs/1702.00403))
6. "Galaxy Image Simulation Using Progressive GANs" ([https://www.adass2019.nl/wp-content/uploads/adass-pdf/Poster170.pdf](https://www.adass2019.nl/wp-content/uploads/adass-pdf/Poster170.pdf))
7. "A Deep Learning Approach for Characterizing
Major Galaxy Mergers"([https://ml4physicalsciences.github.io/2020/files/NeurIPS_ML4PS_2020_11.pdf](https://ml4physicalsciences.github.io/2020/files/NeurIPS_ML4PS_2020_11.pdf))
8. "High-Resolution Image Synthesis and Semantic Manipulation with Conditional GANs" ([https://openaccess.thecvf.com/content_cvpr_2018/papers/Wang_High-Resolution_Image_Synthesis_CVPR_2018_paper.pdf](https://openaccess.thecvf.com/content_cvpr_2018/papers/Wang_High-Resolution_Image_Synthesis_CVPR_2018_paper.pdf))
9. "A Two Stage GAN for High Resolution Retinal Image Generation and Segmentation" ([https://arxiv.org/abs/1907.12296](https://arxiv.org/abs/1907.12296))

## Other references (articles and blogs):

1. "How does an AI Imagine the Universe?"

([https://towardsdatascience.com/how-does-an-ai-imagine-the-universe-d1d01139b50a](https://towardsdatascience.com/how-does-an-ai-imagine-the-universe-d1d01139b50a))

1. "Galaxy Zoo - The Galaxy Challenge" - Kaggle (Contest)

([https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/overview/timeline](https://www.kaggle.com/c/galaxy-zoo-the-galaxy-challenge/overview/timeline))

1. "Deep learning based super resolution, without using a GAN"

([https://towardsdatascience.com/deep-learning-based-super-resolution-without-using-a-gan-11c9bb5b6cd5](https://towardsdatascience.com/deep-learning-based-super-resolution-without-using-a-gan-11c9bb5b6cd5))

1. "Training a GAN" ([https://towardsdatascience.com/generating-your-own-images-with-nvidia-stylegan2-ada-for-pytorch-on-ampere-a80fab52d6b5](https://towardsdatascience.com/generating-your-own-images-with-nvidia-stylegan2-ada-for-pytorch-on-ampere-a80fab52d6b5))