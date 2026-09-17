using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CarShowRm
{
    public partial class Dashboard : Form
    {
        public Dashboard()
        {
            InitializeComponent();
        }

        private void SellersBtn_Click(object sender, EventArgs e)
        {
            Sellers sl = new Sellers();
            sl.Show();
            this.Hide();
        }

        private void CarsBtn_Click(object sender, EventArgs e)
        {
            Cars cr = new Cars();
            cr.Show();
            this.Hide();
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Bill bl = new Bill();
            bl.Show();
            this.Hide();
        }

        private void WarrantyBtn_Click(object sender, EventArgs e)
        {
            Warranty wr = new Warranty();
            wr.Show();
            this.Hide();
        }

        private void ManageCusBtn_Click(object sender, EventArgs e)
        {
            Customers cs = new Customers();
            cs.Show();
            this.Hide();
        }
        private void LogoutBtn_Click(object sender, EventArgs e)
        {
            this.Close();
            login lg = new login();
            lg.Show();
            this.Hide();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Repair rp = new Repair();
            rp.Show();
            this.Hide();
        }
    }
}
