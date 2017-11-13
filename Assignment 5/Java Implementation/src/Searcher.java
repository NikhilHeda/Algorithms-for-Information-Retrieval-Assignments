import java.io.BufferedReader;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

import org.apache.lucene.analysis.Analyzer;
import org.apache.lucene.analysis.standard.StandardAnalyzer;
import org.apache.lucene.document.Document;
import org.apache.lucene.index.DirectoryReader;
import org.apache.lucene.index.IndexReader;
import org.apache.lucene.queryparser.classic.QueryParser;
import org.apache.lucene.search.IndexSearcher;
import org.apache.lucene.search.Query;
import org.apache.lucene.search.ScoreDoc;
import org.apache.lucene.search.TopDocs;
import org.apache.lucene.store.FSDirectory;

public class Searcher {

	private final String indexPath;
	private final String queriesPath;

	public Searcher(String indexPath, String queriesPath) {
		this.indexPath = indexPath;
		this.queriesPath = queriesPath;
	}

	public void search(String field, int hitsPerPage) {
		try {
			IndexReader reader = DirectoryReader.open(FSDirectory.open(Paths.get(this.indexPath)));
			IndexSearcher searcher = new IndexSearcher(reader);

			Analyzer analyzer = new StandardAnalyzer();
			QueryParser parser = new QueryParser(field, analyzer);

			BufferedReader in = Files.newBufferedReader(Paths.get(this.queriesPath), StandardCharsets.UTF_8);
			String queryString = null;
			while ((queryString = in.readLine()) != null) {
				Query query = parser.parse(queryString);
				System.out.println("Searching for: " + query.toString(field));

				TopDocs results = searcher.search(query, hitsPerPage);
				ScoreDoc[] hits = results.scoreDocs;

				int numTotalHits = Math.toIntExact(results.totalHits);
				System.out.println(numTotalHits + " total matching documents");

				int start = 0;
				int end = Math.min(numTotalHits, hitsPerPage);

				for (int i = start; i < end; i++) {
					Document doc = searcher.doc(hits[i].doc);
					String path = doc.get("path");

					// Printing output
					System.out.println((i + 1) + ". " + path + "\n" + getContent(path));
				}
			}
			reader.close();
		} catch (Exception e) {
			System.out.println(" caught a " + e.getClass() + "\n with message: " + e.getMessage());
		}
	}

	private String getContent(String path) throws IOException {
		Path file = Paths.get(path);
		BufferedReader br = Files.newBufferedReader(file);

		StringBuilder content = new StringBuilder();
		String line = null;
		while ((line = br.readLine()) != null)
			content.append(line + "\n");

		return content.toString();
	}

}
