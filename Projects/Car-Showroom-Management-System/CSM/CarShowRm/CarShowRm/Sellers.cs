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
    public partial class Sellers : Form
    {
        public Sellers()
        {
            InitializeComponent();
            Con = new Functions();
            ShowSeller();
            SellersDGV.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
        }

        Functions Con;

        private void ShowSeller()
        {
            try
            {
                SellersDGV.DataSource = null;
                string Query = "select * from EmployeeTbl";
                SellersDGV.DataSource = Con.getData(Query);
                SellersDGV.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error in loading data: " + ex.Message);
            }
        }

        private void AddBtn_Click(object sender, EventArgs e)
        {
            if (SNameTb.Text == "" || PhoneTb.Text == "" || AddressTb.Text == "" || GenCb.SelectedIndex == -1 || EmployeeTypeCb.SelectedIndex == -1 || SelleryTb.Text == "")
            {
                MessageBox.Show("Enter The Seller Details");
            }
            else
            {
                try
                {
                    string SName = SNameTb.Text;
                    string SPhone = PhoneTb.Text;
                    string Geneder = GenCb.SelectedItem.ToString();
                    string SType = EmployeeTypeCb.SelectedItem.ToString();
                    string Address = AddressTb.Text;
                    decimal Salary = Convert.ToDecimal(SelleryTb.Text);
                    string Query = "INSERT INTO EmployeeTbl (EName, EPhone, EDOB, EGen, EType, EAddress, Salary) " +
                                   "VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', {6})";
                    Query = string.Format(Query, SName, SPhone, DOBTb.Value.Date.ToString("yyyy-MM-dd"), Geneder, SType, Address, Salary);
                    Con.setData(Query);
                    MessageBox.Show("Employee Registered Successfully");
                    ShowSeller();
                    SNameTb.Text = "";
                    PhoneTb.Text = "";
                    AddressTb.Text = "";
                    SelleryTb.Text = "";
                }
                catch (Exception Ex)
                {
                    MessageBox.Show("Error: " + Ex.Message);
                }
            }
        }

        private void SellersDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            SNameTb.Text = SellersDGV.SelectedRows[0].Cells[1].Value.ToString();
            PhoneTb.Text = SellersDGV.SelectedRows[0].Cells[2].Value.ToString();
            DOBTb.Value = Convert.ToDateTime(SellersDGV.SelectedRows[0].Cells[3].Value.ToString());
            GenCb.SelectedItem = SellersDGV.SelectedRows[0].Cells[4].Value.ToString();
            EmployeeTypeCb.SelectedItem = SellersDGV.SelectedRows[0].Cells[6].Value.ToString();
            AddressTb.Text = SellersDGV.SelectedRows[0].Cells[5].Value.ToString();
            SelleryTb.Text = SellersDGV.SelectedRows[0].Cells[7].Value.ToString();
        }

        private void EditBtn_Click(object sender, EventArgs e)
        {
            if (SNameTb.Text == "" || PhoneTb.Text == "" || AddressTb.Text == "" || GenCb.SelectedIndex == -1 || EmployeeTypeCb.SelectedIndex == -1 || SelleryTb.Text == "")
            {
                MessageBox.Show("Enter The Seller Details");
            }
            else
            {
                try
                {
                    int ECode = Convert.ToInt32(SellersDGV.SelectedRows[0].Cells[0].Value.ToString());
                    string SName = SNameTb.Text;
                    string SPhone = PhoneTb.Text;
                    string Geneder = GenCb.SelectedItem.ToString();
                    string SType = EmployeeTypeCb.SelectedItem.ToString();
                    string Address = AddressTb.Text;
                    decimal Salary = Convert.ToDecimal(SelleryTb.Text);
                    string Query = "UPDATE EmployeeTbl SET EName = '{0}', EPhone = '{1}', EDOB = '{2}', EGen = '{3}', EType = '{4}', EAddress = '{5}', Salary = {6} WHERE ECode = {7}";
                    Query = string.Format(Query, SName, SPhone, DOBTb.Value.Date.ToString("yyyy-MM-dd"), Geneder, SType, Address, Salary, ECode);
                    Con.setData(Query);
                    MessageBox.Show("Employee Info Updated Successfully");
                    ShowSeller();
                    SNameTb.Text = "";
                    PhoneTb.Text = "";
                    AddressTb.Text = "";
                    SelleryTb.Text = "";
                    GenCb.SelectedIndex = -1;
                    EmployeeTypeCb.SelectedIndex = -1;
                }
                catch (Exception Ex)
                {
                    MessageBox.Show("Error: " + Ex.Message);
                }
            }
        }

        private void DeleteBtn_Click(object sender, EventArgs e)
        {
            if (SNameTb.Text == "" || PhoneTb.Text == "" || AddressTb.Text == "" || GenCb.SelectedIndex == -1 || EmployeeTypeCb.SelectedIndex == -1 || SelleryTb.Text == "")
            {
                MessageBox.Show("Enter The Seller Details");
            }
            else
            {
                try
                {
                    int ECode = Convert.ToInt32(SellersDGV.SelectedRows[0].Cells[0].Value.ToString());
                    string Query = "DELETE FROM EmployeeTbl WHERE ECode = {0}";
                    Query = string.Format(Query, ECode);
                    Con.setData(Query);
                    MessageBox.Show("Employee Date Deleted Successfully");
                    ShowSeller();
                    SNameTb.Text = "";
                    PhoneTb.Text = "";
                    AddressTb.Text = "";
                    SelleryTb.Text = "";
                    GenCb.SelectedIndex = -1;
                    EmployeeTypeCb.SelectedIndex = -1;
                }
                catch (Exception Ex)
                {
                    MessageBox.Show("Error: " + Ex.Message);
                }
            }
        }

        private void ManuBtn_Click(object sender, EventArgs e)
        {
            Dashboard ds = new Dashboard();
            ds.Show();
            this.Hide();
        }
    }
}

