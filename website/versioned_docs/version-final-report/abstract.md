---
id: abstract
title: Abstract
sidebar_label: Abstract
slug: /abstract
---

A web application to identify song sections (i.e. intro, verse, chorus) from uploaded music files. The area of research is Boundary detection detection and song segmentation, a sub-field of music information retrieval. An artificial neural network was developed to detect the boundaries between song sections, using a dataset of 2000 songs. Sections were identified with an F-score accuracy of 70.8% (at the time of going to press) within a specified musical scope of pop and dance, outperforming the state-of-the-art model by 9%. Data was cleaned and pre-processed incrementally in order to optimise the training of the neural network model. A number of approaches were used to subdivide the data, including frames, beats and bars. An automated process was created for identifying the optimal hyperparameters, such as the number of hidden layers, neurons and epochs (the number of times the entire data is passed forward and back again through the layers of the model). The hyperparameter tuning was performed in Google Colab with TPU power. The web application was created with a React frontend. The model was deployed in the cloud, leveraging AWS Lambda and S3 buckets for a serverless, event-driven architecture.
