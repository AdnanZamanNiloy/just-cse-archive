using System;
using System.Collections.Generic;
using System.Text;

namespace Polymorphism
{
    class Program
    {
        public class clsBank
        {
            public bool hasSufficientSavings(clsCustomer oCustomer, double nLoanAmount)
            {
                if (oCustomer.SavingAmount > nLoanAmount)
                    return true;

                return false;
            }
        }

        public class clsCredit
        {
            public bool hasGoodCredit(clsCustomer oCustomer)
            {
                if (oCustomer.CreditAmount <= 500.0)
                    return true;

                return false;
            }
        }

        public class clsLoan
        {
            public bool hasNoBadLoans(clsCustomer oCustomer)
            {
                if (oCustomer.SavingAmount > oCustomer.CreditAmount + 500.0)
                    oCustomer.BadLoan = false;

                return oCustomer.BadLoan;
            }
        }

        public class clsCustomer
        {
            private string _sName;
            private double _nSavingAmount;
            private double _nCreditAmount;
            private bool _bBadLoan;

            public clsCustomer()        // Constructor
            {
                _sName = "";
                _nSavingAmount = 0.0;
                _nCreditAmount = 0.0;
                _bBadLoan = true;
            }

            public string Name         // Properties
            {
                get
                {
                    return _sName;
                }
                set
                {
                    _sName = value;
                }
            }

            public double SavingAmount
            {
                get
                {
                    return _nSavingAmount;
                }
                set
                {
                    _nSavingAmount = value;
                }
            }

            public double CreditAmount
            {
                get
                {
                    return _nCreditAmount;
                }
                set
                {
                    _nCreditAmount = value;
                }
            }

            public bool BadLoan
            {
                get
                {
                    return _bBadLoan;
                }
                set
                {
                    _bBadLoan = value;
                }
            }
        }

        public class clsMortgage
        {
            private clsBank _oBank = new clsBank();
            private clsCredit _oCredit = new clsCredit();
            private clsLoan _oLoan = new clsLoan();

            public bool isEligible(clsCustomer oCustomer, double nLoanAmount)
            {
                Console.WriteLine("{0} applies for USD {1} loan\n", oCustomer.Name, nLoanAmount);

                bool bEligible = false;

                // Check Worthiness

                if (_oBank.hasSufficientSavings(oCustomer, nLoanAmount) && _oCredit.hasGoodCredit(oCustomer) && ! _oLoan.hasNoBadLoans(oCustomer))
                    bEligible = true;

                return bEligible;
            }
        }

        static void Main()
        {
            clsCustomer oCustomer = new clsCustomer();

            oCustomer.Name = "James";
            oCustomer.SavingAmount = 50000;
            oCustomer.CreditAmount = 100;

            clsMortgage oMortgage = new clsMortgage(); // Facade

            double nLoanAmount = 25000;

            bool isEligible = oMortgage.isEligible(oCustomer, nLoanAmount);

            Console.WriteLine("\n" + oCustomer.Name + " has been " + (isEligible ? "Approved." : "Rejected."));

            Console.ReadKey();
        }
    }
}
