# Skin Cancer Classification

This project focuses on classifying skin cancer images using deep learning techniques. It utilizes the HAM10000 dataset, which contains images of various skin lesions.

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Adeyeha/skin_cancer_classification.git
   ```

2. Install dependencies:

    ```python
    pip install -r requirements.txt
    ```
    
## Usage
Modify and run the notebook ```ham10000-skin-disease-classification.ipynb``` to train and evaluate the skin cancer classification model:


## Model Evaluation
The trained model is evaluated on both the validation set and the test set. The evaluation includes metrics such as accuracy, loss, and a confusion matrix. The results are displayed through plots and classification reports.


## Tasks
1. Implement your assigned pre-trained model in ```ham10000-skin-disease-classification.ipynb```
2. Compare evaluation metrics for validation and test.
3. Experiment with different image shape e.g 100 x 100.
4. Experiment with/without random oversampling
5. Experiment with/without standardization of train and test data


## License
This project is licensed under the MIT License.

## Contributing
Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
    ```shell
    git checkout -b feature/new-feature
    ```
3. Make your changes and commit them: 
    ```shell
    git commit -am 'Add new feature'
    ```
4. Push to the branch:
    ```shell
    git push origin feature/new-feature
    ```
5. Submit a pull request.

