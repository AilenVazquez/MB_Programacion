import java.util.Scanner;

public class tp_aplicacion {
    public static void main(String[] args) {
        //1. Pedir el radio de un círculo y calcular su área. A=PI*r^2.
        /* 
            Scanner entrada = new Scanner(System.in);

            Double radio;
        

            System.out.println("Ingrese el radio del círculo: ");

            radio = entrada.nextDouble();

            Double area = Math.PI * Math.pow(radio,2);

            System.out.println("El área del circulo es: "+ area);
        */
        
        //2. Pedir un número e indicar si es positivo o negativo.
        /*
            for(int i=0; i<3; i++){
                Double numero;
                Scanner entrada = new Scanner(System.in);

                System.out.println("Ingrese un número: ");

                numero =  entrada.nextDouble();

                if(numero >= 0){
                    System.out.println("El numero es positivo");
                }else{
                    System.out.println("El numero es negativo");
                }
            }
        */

        //3. Pedir dos números y decir cual es el mayor o si son iguales.
        /* 
            Scanner entrada = new Scanner(System.in);
            int num1, num2;
            System.out.println("Ingrese 2 numeros:");
            num1 = entrada.nextInt();
            num2 = entrada.nextInt();

            if(num1 == num2){
                System.out.println("Los numeros son iguales");
            }
            else if(num1 > num2){
                System.out.println("El numero "+ num1 + " es mayor que el numero " + num2);
            }else{
                System.out.println("El numero "+ num2 + " es mayor que el numero " + num1);
            }
        */
        
        //4. Pedir tres números y mostrarlos ordenados de mayor a menor.
        /* 
            Scanner entrada = new Scanner(System.in);
            int num1, num2, num3;
            System.out.println("Ingrese 3 números distintos: ");
            num1 = entrada.nextInt();
            num2 = entrada.nextInt();
            num3 = entrada.nextInt();
            

            
            //Numero Mayor
            int mayor = num3;

            if(num1 > num2 && num1 > num3){
                mayor = num1;
            }
            if(num2 > num3 && num2 > num1){
                mayor = num2;
            }
            if(num3 > num1 && num3 > num2){
                mayor = num3;
            }

            //Numero Menor
            int menor = num1;

            if(num1 < num2 && num1 < num3){
                menor = num1;
            }
            if(num2 < num3 && num2 < num1){
                menor = num2;
            }
            if(num3 < num1 && num3 < num2){
                menor = num3;
            }

            //Numero Medio
            int medio = num2;
            
            if((menor == num1 && mayor ==num3) || (menor == num3 && mayor == num1)){
                medio = num2;
            }
            if((menor == num1 && mayor ==num2) || (menor == num2 && mayor == num1)){
                medio = num3;
            }
            if((menor == num2 && mayor ==num3) || (menor == num3 && mayor == num2)){
                medio = num1;
            }

            System.out.println("Numeros ordenados de mayor a menor: " + mayor + " " + medio + " " + menor);
        */

        //5. Pedir un número entre 0 y 9.999 y decir cuantas cifras tiene.(No usar String)

        /* 
            Scanner entrada = new Scanner(System.in);
            int numero;
            System.out.println("Ingrese un numero entre el 0 y el 9999: ");
            numero = entrada.nextInt();

            if((numero < 0) || (numero > 9999)){
                System.out.println("El numero no pertenece al rango especificado. Ingrese nuevamente un número: ");
                numero = entrada.nextInt();
            }

            if(numero > 999){
                System.out.println("El numero tiene 4 cifras");
            }else if(numero > 99){
                System.out.println("El numero tiene 3 cifras");
            }else if(numero > 9){
                System.out.println("El numero tiene 2 cifras");
            }else{
                System.out.println("El numero tiene 1 cifra");
            }
        */
        
        //6. Pedir un número entre 0 y 9.999 y mostrarlo con las cifras al revés. (no usar String)

        /* 
            Scanner entrada = new Scanner(System.in);
            int numero;
            System.out.println("Ingrese un numero entre el 0 y el 9999: ");
            numero = entrada.nextInt();

            if((numero < 0) || (numero > 9999)){
                System.out.println("El numero no pertenece al rango especificado. Ingrese nuevamente un número: ");
                numero = entrada.nextInt();
            }

            int cifra1 = (int) Math.abs(numero / 1000);

            int cifra2 = (numero / 100) % 10;

            int cifra3 = (numero / 10) % 10;

            int cifra4 = numero % 10;

            System.out.println("El numero al reves es: "+cifra4+" "+cifra3+" "+cifra2+" "+cifra1);

        */

        //7. Pedir el día, mes y año de una fecha correcta y mostrar la fecha del día siguiente. suponer que todos los meses tienen 30 días

        /* 
            Scanner entrada = new Scanner(System.in);
            int dia, mes, año;

            System.out.println("Ingrese un dia del 1 al 30: ");
            dia = entrada.nextInt();

            if(dia < 1 || dia > 30){
                System.out.println("El dia especificado no existe, intente denuevo: ");
                dia = entrada.nextInt();
            }

            System.out.println("Ingrese el mes en numero: ");
            mes = entrada.nextInt();

            if(mes < 1 || mes > 12){
                System.out.println("El mes especificado no existe, intente denuevo: ");
                mes = entrada.nextInt();
            }

            System.out.println("Ingrese el año en el siguiente formato YYYY: ");
            año = entrada.nextInt();

            if(año < 0){
                System.out.println("El año especificado no existe, intente denuevo: ");
                año = entrada.nextInt();
            }

            if(dia < 30){
                dia++;
            }else if(dia == 30){
                dia = 1;
                if (mes < 12) {
                    mes++;
                }else if(mes == 12){
                    mes = 1;
                    año++;
                }
            }

            System.out.println("El dia siguiente es: "+dia+"-"+mes+"-"+año);
        */    


        //8. Qué hace el siguiente programa?

            String nombre;
            int diaNacimiento, mesNacimiento, añoNacimiento;

            //inicializacion de la instancia de Scanner con el flujo de entrada del teclado

            Scanner entradaTeclado = new Scanner(System.in);

            System.out.print("¿Como te llamas?");
            nombre = entradaTeclado.nextLine();

            System.out.print("¿Que dia naciste?");
            diaNacimiento = entradaTeclado.nextInt();

            System.out.print("¿En que mes?");
            mesNacimiento = entradaTeclado.nextInt();

            System.out.print("¿En que año?");
            añoNacimiento = entradaTeclado.nextInt();

            System.out.println("Hola "+nombre+ ", naciste el "+diaNacimiento+"/"+mesNacimiento+"/"+añoNacimiento);
    }


    
}