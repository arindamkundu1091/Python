class Apple {
    int height;
    int width;
    
    public Apple(int height, int width) {
        this.height = height;
        this.width = width;
    }
    
    public static void main(String[] args) {
        String input = "mammaadaammaa";
        String sub1Reverse, sub2Reverse, answer1="", answer2="", answer="";
        StringBuilder sb1, sb2;
        int lastIndex = input.length(), temp =  0, temp1 = 0, temp2 = 0;
        int firstIndex = 0;
        for(int i =0 ;i <input.length();i++) {
            String sub1 = input.substring(0,firstIndex);
            String sub2 = input.substring(firstIndex,lastIndex-1);
            sb1 = new StringBuilder(sub1);
            sub1Reverse =""+sb1.reverse();
            sb2 = new StringBuilder(sub2);
            sub2Reverse =""+sb2.reverse();
            if(sub1.equals(sub1Reverse)){
                answer1 = sub1;
                temp1 = sub1.length();
            }
            if(sub2.equals(sub2Reverse)){
                answer2 = sub2;
                temp2 = sub2.length();
            }
            if(temp2 > temp1){
                if(temp2 > temp){
                    answer = answer2;
                    temp = temp2;
                }
            }
            else {
                if(temp1 > temp){
                    answer = answer1;
                    temp = temp1;
                }
            }
            firstIndex++;
        }
        if(answer.length()<3){
            System.out.println("There is no palindrome");
        }
        else
        {
            System.out.println(answer+" : "+temp);
        }
    }

}