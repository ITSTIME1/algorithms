package AbstractStudy;

/**
 * 종합정보시스템
 */

 /**
  * 종합정보 시스템은, 학교에서 일어나는 모든 정보를 웹 상에서 볼 수 있는 시스템이다.

  1. 학생과 교직원 교수는 종합정보시스템에 회원가입 및 로그인이 가능해야한다.
  2. 학생은 자신의 정보를 조회할 수 있어야 한다. (개인정보, 수강내역, 성적)
  3. 교직원은 학생목록, 강의목록, 특정학생의 학생정보를 볼 수 있어야 한다.
  4. 교직원은 강의를 등록할 수 있어야 한다.
  5. 교직원은 성적을 처리할 수 있어야 한다.


  1.객체를 구분해보자.
  학생, 교수, 교직원
  회원가입, 로그인
  개인정보, 수강내역, 성적, 강의
  

  2. 객체를 공통된 것끼리 분류해보자.
  학생, 교수, 교직원 -> User로 구분이 가능하다. role 필드를 갖게 되면 학생인지, 교순지알 수 있으니까
  회원가입, 로그인 -> Auth로 구분이 가능하다. 등록과정을 거치기 때문에.
  강의 목록은 클래스를 만든다. -> 하나의 객체로 취급한다.
  수강내역은 학생이 가지고 가지고 있도록 한다.
  강의 -> 등록된 강의들을보여준다.


  3. 엔티티를 만들자.
  User, Auth, Course, Grade


  4. 엔티티가 처리해야 할 사항들으 명시해보자.
  User
    로그인, 회원가입을 할 수 있어야 한다.
    role이 학생이라면 자신의 개인정보와 성적, 강의내역을 조회할 수 있어야 한다.
    role이 교직원이라면 강의를 등록할 수 있어야하고, 학생목록조회가 가능해야 한다.
    role이 교수라면, 학생에게 학점을 부여할 수 있고, 학생목록조회가 가능해야 한다.
    음 그러면 차라리 User를 분리하는게 낫겠다. 공통 관심사도 교직원이랑 교수밖에 없고, 학생은 이들과 공통관심사가 존재하지 않으니까
    아 공통관심사가 존재하긴하네 로그인 회원가입은 모두가 할 수 있으니까 -> 공통관심사로 분리

  */


// Template Method Pattern을 적용하자.
// 즉 공통된 로직은 상위 클래스에서 정의하되 해당 기능을 사용하기 위한 개별기능의 정의는 하위 클래스에서 하는것.
abstract class 회원 {
    void 로그인() {
        특정회원종류별_로그인();
    };
    void 회원가입() {
        특정회원종류별_회원가입();
    };

    abstract void 특정회원종류별_로그인();
    abstract void 특정회원종류별_회원가입();
}
interface StudentManager{}
interface StudentInterface {}
interface ProfessionalInterface {}
interface StaffInterface {}
class 학생 extends 회원 implements StudentInterface{}
class 교수 extends 회원 implements StudentManager, ProfessionalInterface{}
class 교직원 extends 회원 implements StudentManager, StaffInterface{}

public class 종합정보시스템 {

    public static void main(String[] args) {
        
    }
}