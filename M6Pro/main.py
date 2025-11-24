from nltk.corpus import stopwords
import nltk.sentiment
import pandas as pd
from pandas import DataFrame
import nltk
from matplotlib.pyplot as plt

def main() -> None:
    frame: DataFrame = pd.read_csv("movie_reviews.csv", index_col="Movie_Title")
    print(frame)
    for a in frame.index.unique():
        print(a)
        print(frame[frame.index == a])
    frame["Sentiment_Score"] = frame.apply(lambda a: nltk.sentiment.SentimentIntensityAnalyzer().polarity_scores(a["Review"])["compound"], axis=1)
    print(frame)
    frame["Sentiment_Label"] = frame.apply(lambda a: "Positive" if a["Sentiment_Score"] > 0 else ("Negative" if a["Sentiment_Score"] < 0 else "Neutral"), axis=1)
    print(frame)
    #[
    #    nltk.stem.PorterStemmer.stem(a) 
    #    for a in nltk.word_tokenize(a["Review"]) 
    #    if stem := nltk.stem.PorterStemmer.stem(a) not in stopwords.words("english")
    #]
    whoKnows: dict[str, tuple[float, float]] = {}
    for a in frame.index.unique():
        print(frame[frame.index == a])
        whoKnows[a] = (frame[frame.index == a]["Sentiment_Score"].mean(), frame[frame.index == a]["Rating"].mean())
    thingy: DataFrame = DataFrame.from_dict(whoKnows)
    print(thingy)
    plt.show_fig()

if __name__ == "__main__":
    nltk.download("punkt")
    nltk.download('stopwords')
    nltk.download('vader_lexicon')

    main()