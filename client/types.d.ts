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
    tagLine: string;
}

interface FullSnippet extends Snippet {
    parts: Sentence[];
}
