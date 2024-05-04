class StreamTest {
	public static void main(String[] args) {
		// string 타입의 배열이 있다고 하자.
		String[] arr = new String[]{"a", "b", "c"};
		// 스트림을 사용하기 위해서는 배열 또는 컬렉션 인스턴스를 활용해서 만들 수 있다.
		// 따라서 스트림 객체를 먼저 생성해준다.


		// 배열 같은 경우 Arrays.stream 메소드를 이용한다.
		Stream<String> stream = Arrays.stream(arr);

		Stream<String> streamOfArrayPart = Arrays.stream(arr, 1, 3);


		List<String> list = Arrays.asList("a");
		Stream<String> streamString = list.stream();
		Stream<String> parallelStream = list.parallelStream();


		Stream<String> builderStream = Stream.<String>builder().add("Eric").add("Elena").build();
	}
}