import nltk
import smtplib
from email.mime.text import MIMEText
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist

# Download necessary NLTK resources (only needs to be done once)
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')

# Function to connect to Gmail SMTP server
def connect_to_gmail(email_address, password):
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(email_address, password)
        print("Connected to Gmail SMTP successfully.")
        return server
    except Exception as e:
        print(f"Failed to connect to Gmail SMTP: {e}")
        return None

# Function to parse email subject lines and calculate a spam score
def parse_email_subject(subject_line):
    # Tokenize, lowercase, remove stop words, and lemmatize
    lemmatizer = WordNetLemmatizer()
    tokens = [
        lemmatizer.lemmatize(token) for token in word_tokenize(subject_line.lower())
        if token.isalpha() and token not in stopwords.words('english')
    ]

    # Define keywords and their weights (example keywords for spam detection)
    keywords = {
        'win': 5, 'free': 3, 'offer': 2, 'money': 4, 'urgent': 3,
        'click': 2, 'now': 1, 'guaranteed': 4, 'limited': 2, 'exclusive': 1
    }
    
    # Calculate spam score based on keyword frequencies
    spam_score = sum(keywords.get(token, 0) for token in tokens)
    print(f"Tokens: {tokens}\nSpam Score: {spam_score}")

    # Display top keywords with frequencies
    fdist = FreqDist(tokens)
    for word, frequency in fdist.most_common(5):
        print(f"Keyword: {word}, Frequency: {frequency}")

    return spam_score

# Example usage of the script
if __name__ == "__main__":
    # Example email subject line to analyze
    subject = "Win a free gift now! Limited time offer."
    spam_score = parse_email_subject(subject)
    print(f"Final Spam Score for '{subject}': {spam_score}")

    # Attempt to connect to Gmail (replace with real credentials if testing)
    email_address = "your_email@gmail.com"
    password = "your_password"
    server = connect_to_gmail(email_address, password)
    if server:
        server.quit()
