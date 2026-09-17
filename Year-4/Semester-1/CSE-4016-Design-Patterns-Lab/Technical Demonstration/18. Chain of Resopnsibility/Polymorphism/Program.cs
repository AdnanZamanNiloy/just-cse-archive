using System;
using System.Collections.Generic;
using System.Text;

namespace Polymorphism
{
    class Program
    {
        public class clsPurchase
        {
            private int _nNumber;
            private double _nAmount;
            private string _sPurpose;

            public int Number
            {
                get
                {
                    return _nNumber;
                }
                set
                {
                    _nNumber = value;
                }
            }

            public double Amount
            {
                get
                {
                    return _nAmount;
                }
                set
                {
                    _nAmount = value;
                }
            }

            public string Purpose
            {
                get
                {
                    return _sPurpose;
                }
                set
                {
                    _sPurpose = value;
                }
            }

            public clsPurchase(int nNumber, double nAmount, string sPurpose)
            {
                _nNumber = nNumber;
                _nAmount = nAmount;
                _sPurpose = sPurpose;
            }
        }

        public abstract class clsApprover
        {
            protected clsApprover oSuccessor;

            public void setSuccessor(clsApprover oSuccessor)
            {
                this.oSuccessor = oSuccessor;
            }

            public abstract void processRequest(clsPurchase oPurchase);
        }

        public class clsChairman : clsApprover
        {
            public override void processRequest(clsPurchase oPurchase)
            {
                if (oPurchase.Amount <= 25000.0)
                {
                    Console.WriteLine("Chairman approves Purchase {0}", oPurchase.Number);
                }
                else if (oSuccessor != null)
                {
                    oSuccessor.processRequest(oPurchase);
                }
            }
        }

        public class clsTreasurer : clsApprover
        {
            public override void processRequest(clsPurchase oPurchase)
            {
                if (oPurchase.Amount <= 500000.0)
                {
                    Console.WriteLine("Treasurer approves Purchase {0}", oPurchase.Number);
                }
                else if (oSuccessor != null)
                {
                    oSuccessor.processRequest(oPurchase);
                }
            }
        }

        public class clsViceChancellor : clsApprover
        {
            public override void processRequest(clsPurchase oPurchase)
            {
                if (oPurchase.Amount <= 1000000.0)
                {
                    Console.WriteLine("Vice Chancellor approves Purchase {0}", oPurchase.Number);
                }
                else
                {
                    Console.WriteLine("Purchase {0} requires Regent Board Meeting.", oPurchase.Number);
                }
            }
        }

        static void Main(string[] args)
        {
            // Behavioral Design Patterns deal with communication and interaction between objects

            // Setup Chain of Responsibility

            clsApprover oGal = new clsChairman();

            clsApprover oMam = new clsTreasurer();

            clsApprover oMaz = new clsViceChancellor();

            oGal.setSuccessor(oMam);
            oMam.setSuccessor(oMaz);

            // Generate and process purchase requests

            clsPurchase oPurchase = new clsPurchase(777, 350000.00, "Research");
            oGal.processRequest(oPurchase);

            oPurchase = new clsPurchase(888, 800000.00, "Construction");
            oGal.processRequest(oPurchase);

            oPurchase = new clsPurchase(999, 3060000000.00, "ADB Project");
            oGal.processRequest(oPurchase);

            Console.ReadKey();

            Console.ReadLine();
        }
    }
}
