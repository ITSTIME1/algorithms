
// Comparator는 두 객체를 비교
// 파라미터로 두 개의 객체를 받게 됨
// 따라서 두 개의 객체를 가지고 정렬을 함.
// Comparator객체는 util 패키지에 존재하기 때문에 import 가 필요하고
// Comparable은 lang 패키지에 존재하기 때문에, 별도의 import 과정이 필요가 없음
import java.util.Comparator;

class Student implements Comparator<Student>{
	private int age;
	private String name;
	private int year;

	@Override
	public int compareTo(Student o1, Student o2) {
		
	}
}

class ComparableTest implements Comparable<Student>{
	// Comparable은 해당 CompareTo 메서드를 호출한, 객체자신과
	// 호출한 객체와 타입이 같은, 객체를 파라미터로 받아서 비교한다.

	@Override
	public int compareTo(Student o) {
		// 만약 나이를 기준으로 정렬을 하고 싶다면 어떻게 해야 할까
		// 이 때 자기 자신을 기준으로 삼아, 정렬을 해야 한다.
		// 이렇게 하게 되면, 호출한 객체를 기준으로
		// 호출한 객체의 나이가 더 많다면, 양수를
		// 서로 같다면 0을
		// 만약 파라미터 나이가 더 크다면, 음수를 보낸다.
		// 기본형 데이터 범위가 넘어가는지를 체크해야 되겠네
		return this.age - o.age;

	}
	public static void main(String[] args) {
		
	}
}
