import java.util.Scanner;

public class arrays{
    public static void main(String[] args) {

        int[] numeros;
        int i;

        numeros = new int[5];
        
        for( i=0; i<5;i++){
            numeros[i] = (int)(Math.random() * (10 - 0));
            System.out.print(numeros[i]+" ");
        }

        for(int j=0; j<4; j++){
            for(i=0; i<4; i++){
                if(numeros[i] > numeros[i+1]){
                    int num = numeros[i];
                    numeros[i] = numeros[i+1];
                    numeros[i+1] = num;
                }
            }
        }
        
        System.out.println("");  
        for(i=0; i<5;i++){
             System.out.print(numeros[i]);
        }
           
    }       
}
