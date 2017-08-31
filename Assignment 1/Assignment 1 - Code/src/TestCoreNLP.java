import edu.stanford.nlp.pipeline.*;

import java.io.PrintWriter;
import java.util.*;

public class TestCoreNLP {

	public static void main(String[] args) {
		// Setting Properties
		Properties props = new Properties();
		props.setProperty("annotators", "tokenize, ssplit, pos, lemma, ner, parse, dcoref");
		
		// Creating a pipeline
		StanfordCoreNLP pipeline = new StanfordCoreNLP(props);
		
		// Reading text
		String text = "Hi this is Nikhil Heda.";
		
		// Create empty annotation with the given text
		Annotation document = new Annotation(text);
		
		// Running the Annotators on this.
		pipeline.annotate(document);
		
		pipeline.prettyPrint(document, new PrintWriter(System.out));
	}

}