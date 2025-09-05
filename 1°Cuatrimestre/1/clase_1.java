import java.util.Scanner;

public class clase_1 {

    public static void main(String[] args) {
        //CLASE DE PROGRAMACION
        Scanner teclado = new Scanner(System.in);

        int numero;

        System.out.println("Ingrese un numero");
        numero = teclado.nextInt();
        if(numero%2 == 0){
            System.out.println("El numero es par");
        }else{
            System.out.println("El numero es impar");
        }
        
        String nombre=teclado.nextLine();
        System.out.println("Ingrese la nota de "+nombre);
        int nota=teclado.nextInt();
        if(nota>=6){
            System.out.println("Aprobado");
        }else{
            System.out.println("Desaprobado");
        }
        
    }
}