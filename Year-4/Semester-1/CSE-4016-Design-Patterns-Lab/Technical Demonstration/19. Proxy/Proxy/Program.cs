using System;

class Program
{
    public interface ICar
    {
        void driveCar();
    }

    // Real Objects

    public class clsCar : ICar
    {
        public void driveCar()
        {
            Console.WriteLine("He is permitted to drive a car.");
        }
    }

    public class clsDriver
    {
        public int Age { get; set; }

        public clsDriver(int nAge)
        {
            this.Age = nAge;
        }
    }

    //Proxy Object

    public class clsProxyCar : ICar
    {
        private clsDriver oDriver;
        private ICar oRealCar;

        public clsProxyCar(clsDriver oDriver)
        {
            this.oDriver = oDriver;
            this.oRealCar = new clsCar();
        }

        public void driveCar()
        {
            if (oDriver.Age <= 16)
                Console.WriteLine("He is not permitted to drive a car.");
            else
                this.oRealCar.driveCar();
        }
    }

    public static void Main()
    {
        ICar oCar = new clsProxyCar(new clsDriver(16));
        oCar.driveCar();

        oCar = new clsProxyCar(new clsDriver(25));
        oCar.driveCar();

        Console.ReadKey();
    }
}
