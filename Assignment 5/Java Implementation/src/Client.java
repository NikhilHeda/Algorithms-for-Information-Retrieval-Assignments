import java.util.Date;

public class Client {

	public static void main(String[] args) {
		final String docsPath = "C:\\Users\\prakash\\Desktop\\Assignment 5\\Data";
		final String indexPath = "C:\\Users\\prakash\\Desktop\\Assignment 5\\Index";
		final String queriesPath = "C:\\Users\\prakash\\Desktop\\Assignment 5\\queries.txt";
		String field = "contents";
		int hitsPerPage = 25;

		// Indexing
		Indexer indexer = new Indexer(docsPath, indexPath);
		Date start = new Date();
		indexer.index();
		Date end = new Date();
		System.out.println("Time taken to index: " + (end.getTime() - start.getTime()) + " milliseconds");

		// Searching
		Searcher searcher = new Searcher(indexPath, queriesPath);
		searcher.search(field, hitsPerPage);
	}

}
