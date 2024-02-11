import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.HashMap;
import java.util.List;
import java.util.StringTokenizer;
import java.util.Comparator;

// Word 클래스를 하나 만들어서
class  Word {
    private String wordName;
    private int wordSize;
    private int wordCount;

    Word(String name) {
        this.wordName = name;
        this.wordSize = this.wordName.length();
        this.wordCount = 1; // 단어가 생성될 때 카운트를 1로 초기화합니다.
    }

    public String getName() {
        return wordName;
    }

    public int getSize() {
        return wordSize;
    }

    public int getWordCount() {
        return wordCount;
    }

    public void increaseCount() {
        wordCount++; // 등장 횟수를 증가시킵니다.
    }
}

public class 영단어단기는괴로워 {
    public static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    public static StringBuilder sb = new StringBuilder();
    public static void run() throws IOException {

        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        HashMap<String, Word> wordMap = new HashMap<>();

        for (int i = 0; i < N; i++) {
            String word = br.readLine();
            
            if (word.length() >= M) {
                if (wordMap.containsKey(word)) {
                    wordMap.get(word).increaseCount();
                } else {
                    wordMap.put(word, new Word(word));
                }
            }
        }

        List<Word> wordList = new ArrayList<>(wordMap.values());

        // comparator를 anonymous instance로 만들어서, 정렬을 하려고 함.
        Comparator<Word> com = new Comparator<Word>() {
            @Override
            public int compare(Word o1, Word o2) {
                
                if(o1.getWordCount() != o2.getWordCount()){
                    return o2.getWordCount() - o1.getWordCount();
                } else if(o1.getSize() != o2.getSize()) {
                    return -(o1.getSize() - o2.getSize());
                    // return o2.getSize() - o1.getSize();
                }
                return o1.getName().compareTo(o2.getName());
            }
        };
        // // 정렬
        // // Comparator를 구현
        // Collections.sort(wordList, new Comparator<Word>() {
        //     @Override
        //     public int compare(Word o1, Word o2) {
        //         // 자주 등장하는 단어 순서대로 정렬
        //         if (Integer.compare(o2.getWordCount(), o1.getWordCount()) != 0) {
        //             return Integer.compare(o2.getWordCount(), o1.getWordCount());
        //         }
        //         // 등장 횟수가 같으면 길이가 긴 단어가 먼저 오도록 정렬
        //         if (o1.getSize() != o2.getSize()) {
        //             return Integer.compare(o2.getSize(), o1.getSize());
        //         }
        //         // 등장 횟수와 길이가 같으면 사전 순으로 정렬
        //         return o1.getName().compareTo(o2.getName());
        //     }
        // });

        // 그럼 Collections.sort와 Arrays sort는 무엇이 다르낙.
        Collections.sort(wordList, com);
        // 결과를 StringBuilder에 저장
        for (Word word : wordList) {
            sb.append(word.getName()).append("\n");
        }

        // 결과 출력
        System.out.print(sb.toString());
    }
    public static void main(String[] args) throws IOException {
        run();
    }
}
