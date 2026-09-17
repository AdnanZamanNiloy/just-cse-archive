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
    public partial class Customers : Form
    {
        public Customers()
        {
            InitializeComponent();
            Con = new Functions();
            ShowCustomers();
            CustomersDGV.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
        }
        Functions Con;

        private void ShowCustomers()
        {
            try
            {
                CustomersDGV.DataSource = null;
                string Query = "select * from CustomerTbl";
                CustomersDGV.DataSource = Con.getData(Query);
                CustomersDGV.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error in loading data: " + ex.Message);
            }
        }

        private void AddBtn_Click(object sender, EventArgs e)
        {
            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || EmailTb.Text == "" || PurchaseTb.Text == " " || GenCb.Text == " ")
            {
                MessageBox.Show("Enter The Customer Details");
            }
            else
            {
                try
                {
                    string Name = NameTb.Text;
                    string Phone = PhoneNumberTb.Text;
                    string Email = EmailTb.Text;
                    string Purchase = PurchaseTb.Text;
                    string Gen = GenCb.Text;
                    string Query = "INSERT INTO CustomerTbl VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}')";
                    Query = string.Format(Query, Name, Phone, Email, Gen, Purchase, PDTb.Value.Date.ToString("yyyy-MM-dd"));
                    Con.setData(Query);
                    MessageBox.Show("Customer Added Successfully");
                    ShowCustomers();
                    NameTb.Text = "";
                    PhoneNumberTb.Text = "";
                    EmailTb.Text = "";
                    PurchaseTb.Text = "";
                    GenCb.Text = "";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error: " + ex.Message);
                }
            }
        }

        private void CustomersDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            NameTb.Text = CustomersDGV.SelectedRows[0].Cells[1].Value.ToString();
            PhoneNumberTb.Text = CustomersDGV.SelectedRows[0].Cells[2].Value.ToString();
            EmailTb.Text = CustomersDGV.SelectedRows[0].Cells[3].Value.ToString();
            GenCb.Text = CustomersDGV.SelectedRows[0].Cells[4].Value.ToString();
            PurchaseTb.Text = CustomersDGV.SelectedRows[0].Cells[5].Value.ToString();
            PDTb.Value = Convert.ToDateTime(CustomersDGV.SelectedRows[0].Cells[6].Value.ToString());

        }

        private void EditBtn_Click(object sender, EventArgs e)
        {
           
            if (CustomersDGV.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a customer to edit.");
                return;
            }

            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || EmailTb.Text == "" || PurchaseTb.Text == " " || GenCb.Text == " ")
            {
                MessageBox.Show("Enter the customer details to update.");
                return;
            }

            try
            {
                int Id = Convert.ToInt32(CustomersDGV.SelectedRows[0].Cells[0].Value.ToString());
                string Name = NameTb.Text;
                string Phone = PhoneNumberTb.Text;
                string Email = EmailTb.Text;
                string Purchase = PurchaseTb.Text;
                string Gen = GenCb.Text;
                string PurchaseDate = PDTb.Value.Date.ToString("yyyy-MM-dd");
                string Query = "UPDATE CustomerTbl SET Name = '{0}', PhoneNumber = '{1}', Email = '{2}', Gender = '{3}', PurchaseItemD = '{4}', PurchaseDate = '{5}' WHERE Id = {6}";
                Query = string.Format(Query, Name, Phone, Email, Gen, Purchase, PurchaseDate, Id);

                Con.setData(Query);
                MessageBox.Show("Customer details updated successfully.");
                ShowCustomers();
                NameTb.Text = "";
                PhoneNumberTb.Text = "";
                EmailTb.Text = "";
                PurchaseTb.Text = "";
                GenCb.Text = "";
                PDTb.Value = DateTime.Now;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void DeleteBtn_Click(object sender, EventArgs e)
        {
            if (CustomersDGV.SelectedRows.Count == 0)
            {
                MessageBox.Show("Please select a customer to edit.");
                return;
            }

            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || EmailTb.Text == "" || PurchaseTb.Text == " " || GenCb.Text == " ")
            {
                MessageBox.Show("Enter the customer details to update.");
                return;
            }

            try
            {
                int Id = Convert.ToInt32(CustomersDGV.SelectedRows[0].Cells[0].Value.ToString());
                string Name = NameTb.Text;
                string Phone = PhoneNumberTb.Text;
                string Email = EmailTb.Text;
                string Purchase = PurchaseTb.Text;
                string Gen = GenCb.Text;
                string PurchaseDate = PDTb.Value.Date.ToString("yyyy-MM-dd");
                string Query = "Delete from CustomerTbl WHERE Id = {0}";
                Query  = string.Format(Query, Id);

                Con.setData(Query);
                MessageBox.Show("Customer details Deleted successfully.");
                ShowCustomers();
                NameTb.Text = "";
                PhoneNumberTb.Text = "";
                EmailTb.Text = "";
                PurchaseTb.Text = "";
                GenCb.Text = "";
                PDTb.Value = DateTime.Now;
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }
        }

        private void button1_Click(object sender, EventArgs e)
        {
            Dashboard dashboard = new Dashboard();
            dashboard.Show();
            this.Hide();
        }
    }
}
