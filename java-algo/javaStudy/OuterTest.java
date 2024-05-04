class OuterTest{
	private int x = 1;
	private static int y = 2;
	private InnerTest innerTest;

	OuterTest () {	
		innerTest = new InnerTest();

	}

	public InnerTest getInnerTest () {
		return this.innerTest;
	}
	public void outerMethod() {
		System.out.println("outerMethod");
	}


	public static void staticOuterMethod() {
		System.out.println("staticOuterMethod");
	}


	// inner class는 외부 클래스가 생성된 후
	// 생성이 되어야 하기 때문에
	// OuterTest가 초기화 되면 위 클래스들이 초기화 된다고 보면 되겠다.
	class InnerTest {
		InnerTest(){}


		public void innerMethodForVariable() {
			System.out.println("outerTest instance variable : " + x);
			outerMethod();

		}

		public void innerMethodForStaticVariable () {
			System.out.println("outerTest instance Variable : " + x);			
			System.out.println("outerTest static Variable : " + y);
		}

	}
	// Test 목적은 inner class 접근 방식
	// inner class가, outerTest의 정적변수 그리고 정적메소드에 접근이 가능하지.	
	// inner class가, outerTest의 인스턴스 변수 그리고 인스턴스 메서드에 접근이 가능한지.
	public static void main(String[] args) {
		OuterTest outTer = new OuterTest();
		outTer.innerTest.innerMethodForVariable();
		outTer.innerTest.innerMethodForStaticVariable();
	}
}