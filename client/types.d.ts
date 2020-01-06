interface Sentence {
    id: number;
    body: string;
}

interface SimilarSentence extends Sentence {
    score: number;
}

interface SimilarResult {
    original: Sentence;
    similar: SimilarSentence[];
}

interface Snippet {
    id: number;
    count: number;
    headline: string;
}

interface FullSnippet extends Snippet {
    sentences: Sentence[];
}
