# Word Cloud Generator for Wikipedia Articles

This project is designed to download any Wikipedia article from an API, process the content, and generate both a **Word Cloud** and a **Column Chart** displaying the most frequent words found in the article.

## Features

- Download a single article based on the title provided as a command-line argument.
- Traverse the JSON response and extract deeply nested sections and paragraphs.
- Generate a Word Cloud of the most common words in the article.
- Display a Column Chart of word frequencies.

## Output
### Word Cloud - Most Frequent
![alt text](image.png)

### Column Chart - Word Frequency
![alt text](image-1.png)

## Usage

### 1. Download an article
To download a single article, use the following command, replacing `"Josephine_Baker"` with the title of the article you want to download:

```bash
python -m word-cloud.get "Josephine_Baker"
```

### 2. Parse and generate visualizations
To extract the text from the article and generate the **Word Cloud** and **Column Chart**, run:

```bash
python -m word-cloud.parse "Josephine_Baker"
```



## License

This project is licensed under the MIT License.
