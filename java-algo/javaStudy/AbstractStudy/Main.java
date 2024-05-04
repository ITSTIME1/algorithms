package AbstractStudy;

interface DuckInterface {
    void 날다();
    void 헤엄치다();
}

class 오리 implements DuckInterface{
    private String name;

    public 오리(String name) {
        this.name = name;
    }
    @Override
    public void 날다() {
        System.out.println(this.name + " : " + " 오리가 날개로 날아갑니다.");
    }

    @Override
    public void 헤엄치다() {
        System.out.println(this.name + " : " +  " 오리가 오리발로 헤엄칩니다.");   
    }

    public String getName() {
        return name;
    }
    
}



class 청둥오리 extends 오리  {

    public 청둥오리(String name) {
        super(name);
    }
}

class 흰오리 extends 오리 {

    public 흰오리(String name) {
        super(name);
    }
}

class 고무오리 extends 오리 {

    public 고무오리(String name) {
        super(name);
    }

    @Override
    public void 날다() {
        System.out.println(super.getName() + " : " + " 저는 날 수 없어요");
    }

    @Override
    public void 헤엄치다() {
        System.out.println(super.getName() + " : " + "오리가 둥둥 떠다닙니다.");
    }

    
    
}

class 고무2오리 extends 오리 {

    public 고무2오리(String name) {
        super(name);
    }

    
    @Override
    public void 날다() {
        System.out.println(super.getName() + " : " + " 저는 날 수 없어요");
    }

    @Override
    public void 헤엄치다() {
        System.out.println(super.getName() + " : " + "오리가 둥둥 떠다닙니다.");
    }
}

class 아수라오리 extends 오리 {

    public 아수라오리(String name) {
        super(name);
    }

    @Override
    public void 헤엄치다() {
        System.out.println(super.getName() + " : " + "오리가 둥둥 떠다닙니다.");
    }
    
    
}

public class Main {
    private static final String ORIGINAL_ORI = "오리지널오리";
    private static final String MALLAD_ORI = "청둥오리";
    private static final String WHITE_ORI = "흰오리";
    private static final String RUBBER_ORI = "고무오리";
    private static final String RUBBER_TWO_ORI = "고무2오리";
    private static final String ASURA_ORI = "아수라오리";

    public static void main(String[] args) {
        오리 originalOri = new 오리(Main.ORIGINAL_ORI);
        originalOri.날다();

        청둥오리 mallardOri = new 청둥오리(Main.MALLAD_ORI);
        mallardOri.날다(); 
        mallardOri.헤엄치다();

        흰오리 whiteOri = new 흰오리(Main.WHITE_ORI);
        whiteOri.날다(); 
        whiteOri.헤엄치다();

        고무오리 rubberOri = new 고무오리(Main.RUBBER_ORI);
        rubberOri.날다(); 
        rubberOri.헤엄치다();

        고무2오리 rubber2Ori = new 고무2오리(Main.RUBBER_TWO_ORI);
        rubber2Ori.날다();
        rubber2Ori.헤엄치다();

        아수라오리 asuraOri = new 아수라오리(Main.ASURA_ORI);
        asuraOri.날다(); 
        asuraOri.헤엄치다();
    }
}
