
abstract class 강사  {
    public void 강사료( ){}
}

class 타이머강사 extends ParentTest{
    @Override
    public void 강사료( ){
        // ..
    }
}


/**
 * ParentTest
 */
class ParentTestClass {
    private int money;
    public void 강사료() {
        this.money = 10000;

    }
    public int getMoney( ){
        return this.money;
    }

    public void setMoney (int money) {
        this.money = money;
    }
}
class ChildTestClass extends ParentTestClass{
    @Override
    public void 강사료( ){
        setMoney(20000);
    }
}
public class ParentTest {

    public static void main(String[] args) {
        ParentTestClass parentTestClass = new ParentTestClass();
        parentTestClass.강사료();
        System.out.println("부모 - 강사료 : " + parentTestClass.getMoney());
        ParentTestClass childTestClass = new ChildTestClass();
        childTestClass.강사료();
        System.out.println("자식 - 강사료 : " + childTestClass.getMoney());
    }
}