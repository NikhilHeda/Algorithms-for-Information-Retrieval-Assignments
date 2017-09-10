import edu.stanford.nlp.pipeline.*;
import edu.stanford.nlp.simple.Document;
import edu.stanford.nlp.simple.Sentence;
//import edu.stanford.nlp.process.Morphology;

import java.io.PrintWriter;
import java.util.*;

public class TestCoreNLP {
	public static void main(String args[]) {
		String text = "I am studying. Hi how are you?";

		Document doc = new Document(text);

		System.out.println("**********Sentece Tokenisation**********");
		List<Sentence> sentences = doc.sentences();
		sentences.stream().forEach(System.out::println);

		System.out.println("**********Word Tokenisation**********");
		for (Sentence sentence : sentences) {
			List<String> words = sentence.words();
			for (String word : words)
				System.out.print("$" + word + "$" + "\t");
			System.out.println();
		}

		System.out.println("**********Lemmatization**********");
		for (Sentence sentence : sentences) {
			List<String> lemmas = sentence.lemmas();
			for (String lemma : lemmas)
				System.out.print("$" + lemma + "$" + "\t");
			System.out.println();
		}
		/*
		 * System.out.println("**********Stemming**********"); for(Sentence
		 * sentence: sentences) { List<String> tags = sentence.posTags();
		 * List<String> words = sentence.words();
		 * 
		 * int upper_bound = tags.size();
		 * 
		 * for(int i = 0; i < upper_bound; i++) {
		 * 
		 * System.out.print(Morphology.stemStatic(words.get(i), tags.get(i)) +
		 * "\t");
		 * 
		 * } System.out.println(); }
		 */

		Properties props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, pos, lemma, ner, parse, dcoref");

		// Creating a pipeline
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);

		// Create empty annotation with the given text
		Annotation document = new Annotation(text);

		// Running the Annotators on this.
		pipeline.annotate(document);

		pipeline.prettyPrint(document, new PrintWriter(System.out));

	}
}