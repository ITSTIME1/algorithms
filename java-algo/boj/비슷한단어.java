import java.io.*;
import java.util.*;


//abca
//zbxz


public class 비슷한단어 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		String[] words = new String[N]; //N개의 단어
		
		for(int i=0;i<N;i++)
			words[i] = br.readLine();
		
		int cnt = 0; //비슷한 단어 쌍 (정답)
		
		for(int i=0;i<N - 1;i++) {		//단어 A
			for(int j=i+1;j<N;j++) {		//단어 B
				boolean flag = true;
				HashMap<Character,Character> map = new HashMap<>(); //숌스럽게 바꾼 문자 저장
				for(int k=0;k<words[j].length();k++) {	//단어 A와 단어 B의 문자열 탐색
					char origin = words[i].charAt(k); //단어 A의 원본 문자열
					char compare = words[j].charAt(k); //숌스럽게 바꾼 단어 B의 문자열
					if(map.containsKey(origin)) { //원본 문자열이 이미 있을 경우(숌하게 바꾼 적 O)
                        // 원본문자열이 또 나왔을때, 그 문자열이 map에 있다면 숌하다는 거고
                        // 숌할때, 해당 compare값이, 매칭이 된 단어랑 검사를 했는데,
                        // 숌하지 않다라는것은, 이미 매칭단어가 숌하고, 그럼 숌하게 바뀌었을때, 
                        // 해당 단어가, B에 있는 단어랑 틀리다면 숌하게 바꾸었는데도, B랑 틀린거니가
                        // flag = false가 됨.
                        // 아 이걸 이렇게 처리하는구나.
						if(map.get(origin)!=compare) { //숌하지 않을 경우
							flag=false;
							break;
						}
					}
                    //abca
                    //zbx 
                    //zbxd
                    // 이때 a는 숌하게 바뀐 이력이 존재하고, 그 단어는 B단어에서 z단어임.
                    // 그러므로 숌하게 바뀐 상태를 보면 zbcz가 되고, zbxd와 비교했을때 b단어의 compare랑 숌하게 변경을 했는데도 불구하고, b단어와 다르게 됨.
                    // 나는 한번에 비교할려고 했던거고, 이 코드는 하나씩 비교 한거네,
                    // 즉 마지막에 비교 했을때, 숌하게 바뀐 상태에서 B단어랑 비교해서 다르다면, 어떤 문자 혹은 문자들이 다르다는걸 알 수 있고
                    // 이렇게 단어별로 확인을 하게 된다면, 숌하게 바뀐 이력이 있고, 그 숌하게 바뀐 이력이 있다면 문자가 B단어의 어떤 문자와 치환이 이루어졌다는걸 의미하니까
                    // 숌하게 바뀌었다면 이라는 전제조건에 만족을하게되고, 그 조건이 만족했을대 B단어가 되냐라는 질문을 다시 한번 생각해본다면
                    // 치환후에 바뀐 단어가 현재 B단어가 가리키는 알파벳과 동일해야하지만, 만약 동일하지 않다면, 숌하게 바궜다라는 전제조건을 만족함에도 불구하고
                    // B단어와는 다르다는 것을 알 수 있지. 다른 단어랑 짝이 지어졌으니까
                    // 그러므로 이런 경우 단어를 완성해도 해당 단어위치에 있는 것이 성립하지 않으므로, 전체를 봤었을때도, 성립을 하지 않는거지.

                    
                    // 그러므로 이건 숌하게 바꾼뒤에, B단어가 된다고 볼 수 없음.
					else { //단어 A의 원본 문자열의 숌스럽게 바꾼 것이 없는 경우
                        // A의 원본 문자열이 숌스럽게 바꾼것이 없는경우.
						Iterator<Character> keys = map.keySet().iterator();
                        // keys에 아무거도 없을 수 있지만 있을 수도 있으니까
						while(keys.hasNext()) {
							char key = keys.next();
                            // map에 value를 가지고 오니까 origin -> compare쌍을 검사하려는경우이고
							if(map.get(key)==compare) { //이미 다른 알파벳의 대체 알파벳일 경우
								flag=false;
								break;
							}
						}
                        // 그럼 처음엔 아무것도 없으니까 while문을 돌지 않을거고
                        // 그렇다면 flag가 true를 유지하고 있으므로, 아래 if분기문의 조건에 맞게 되고
                        // origin 문자를 -> compare로 바꿔줌.
                        // 그럼 a, b, c까지도 마찬가지로 바뀌겠지
                        // b부터는 keys에 1개이상 존재하기 때문에, 검사를 하게 되고
                        // a : z 이런식으로 저장이 되어 있을거니까
                        // 그럼 a의 value가 z이며 두번째로 비교하는 b는 b를 비교하고 있으므로
                        // a라는 키를 가지고 와서 그 값이 compare랑 같다면 지금 비교하고 있는 단어는 A단어 key의 숌하게 바뀐적이 있는 상이 있는 단어이므로
                        // 해당 단어는 바뀌지 못한다는것. 그러므로 flag = false로 만들어서 whiel문을 종료시킴.
                        // 또 origin 이 그럼 b인데, compare로 바꿀 수 있느냐의 질문에, -> no가 됨. 이미 숌하게 바뀐 이력이 존재하기 때문에

                        // 그럼 이러한 A단어에 대해서, compare가 저장이 안됨.
						if(flag)
							map.put(origin, compare);
					}
				}
                // 그럼 하게 바꾼 단어들이라면, flag = false가 될 리가 없음.
                // 그럼 모두 검사를 진행 했을때, flag = true가 되므로, cnt++증가시켜서, 쌍을 만들어줌
                // 오 똑똑해..

				if(flag)
					cnt++;
			}
		}
		System.out.println(cnt);
		
	}
}