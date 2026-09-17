using System;
using System.Collections.Generic;
using System.Text;

namespace Polymorphism
{
    class Program
    {
        public interface ISwitchableDevice
        {
            void TurnOn();
            void TurnOff();
        }

        public class clsLightBulb : ISwitchableDevice
        {
            public bool isLit { get; private set; }
            public int nWattage { get; private set; }
            public string Manufacturer { get; private set; }

            public clsLightBulb(int wattage, string manufacturer)
            {
                nWattage = wattage;
                Manufacturer = manufacturer;
                isLit = false;
            }

            private void Luminate()
            {
                isLit = true;
                Console.WriteLine(nWattage + " watt LightBulb is lit.");
            }

            private void Deluminate()
            {
                isLit = false;
                Console.WriteLine("Now it is Dark.");
            }

            public void TurnOn()
            {
                Luminate();
            }

            public void TurnOff()
            {
                Deluminate();
            }
        }

        public class clsFan : ISwitchableDevice
        {
            public bool isRotate { private set; get; }

            public clsFan()
            {
                isRotate = false;
            }

            private void startRotate()
            {
                isRotate = true;

                Console.WriteLine("The fan is rotating in full speed.");
            }

            private void stopRotate()
            {
                isRotate = false;

                Console.WriteLine("The fan is turned off. Enjoy the summer.");
            }

            public void TurnOn()
            {
                startRotate();
            }

            public void TurnOff()
            {
                stopRotate();
            }

        }

        public class Switch
        {
            public bool IsOn { get; private set; }

            public ISwitchableDevice ConnectedDevice { get; set; }

            public Switch(ISwitchableDevice oConnectedDevice)
            {
                ConnectedDevice = oConnectedDevice;
                IsOn = false;
            }

            public void SwitchOn()
            {
                IsOn = true;
                ConnectedDevice.TurnOn();
            }

            public void SwitchOff()
            {
                IsOn = false;
                ConnectedDevice.TurnOff();
            }
        }

        static void Main(string[] args)
        {
            clsLightBulb oBulb = new clsLightBulb(100, "Philips");
            Switch aSwitch = new Switch(oBulb);

            aSwitch.SwitchOn();

            aSwitch.SwitchOff();

            Console.ReadLine();

            clsFan oFan = new clsFan();

            aSwitch.ConnectedDevice = oFan;

            aSwitch.SwitchOn();

            aSwitch.SwitchOff();

            Console.ReadLine();
        }
    }
}