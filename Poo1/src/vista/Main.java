package vista;

import Model.Curso;
import Model.Estudiante;
import Model.Profesor;

public class Main {
    public static void main(String[] args) {



    Profesor prof1 = new Profesor("Felipe", 47, "Fisica cuantica");
        Profesor prof2 = new Profesor("Andrea", 34, "Historia de España");



    Estudiante est1 = new Estudiante("Antonio", 25, "Ingeniería informatica");
        Estudiante est2 = new Estudiante("Cristina", 24, "enfermeria");
        Estudiante est3 = new Estudiante("Roberto", 28, "magisterio");


        
    Curso curso1 = new Curso("daw", prof1);
        Curso curso2 = new Curso("dam", prof2);







curso1.matricularEstudiante(est1);
    curso1.matricularEstudiante(est2);
    curso2.matricularEstudiante(est3);




curso1.mostrarProfesor();
    curso1.mostrarEstudiantes();
curso2.mostrarProfesor();
    curso2.mostrarEstudiantes();





prof1.trabajar();
    prof2.trabajar();
    }
}