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
    public partial class Warranty : Form
    {
        public Warranty()
        {
            InitializeComponent();
            Con = new Functions();
            ShowWarranty();
            WarrantyDGV.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
        }
        Functions Con;
        private void ShowWarranty()
        {
            try
            {
                WarrantyDGV.DataSource = null;
                string Query = "select * from WarrantyTbl";
                WarrantyDGV.DataSource = Con.getData(Query);
                WarrantyDGV.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error in loading data: " + ex.Message);
            }
        }
        private void AddBtn_Click(object sender, EventArgs e)
        {
            if(NameTb.Text == "" || PhoneNumberTb.Text == "" || GenCb.Text == "" || WarrentyTb.Text == ""|| DetailsTb.Text=="")
            {
                MessageBox.Show("Enter The Warranty Details");
            }
            else
            {
                try
                {
                    string Name = NameTb.Text;
                    string Phone = PhoneNumberTb.Text;
                    string Gen = GenCb.Text;
                    string Warrenty = WarrentyTb.Text;
                    string Details = DetailsTb.Text;
                    string Sta = StatusCb.Text;
                    string Query = "INSERT INTO WarrantyTbl VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')";
                    Query = string.Format(Query, Name, Phone, Gen, Warrenty,Sta, SDateTb.Value.Date.ToString("yyyy-MM-dd"), EDateTb.Value.Date.ToString("yyyy-MM-dd"), Details);
                    Con.setData(Query);
                    MessageBox.Show("Warranty Added Successfully");
                    ShowWarranty();
                    NameTb.Text = "";
                    PhoneNumberTb.Text = "";
                    GenCb.Text = "";
                    WarrentyTb.Text = "";
                    DetailsTb.Text = "";
                    StatusCb.Text = "";
                        
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error in adding Warranty: " + ex.Message);
                }
            }
        }

        private void WarrantyDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            NameTb.Text = WarrantyDGV.SelectedRows[0].Cells[1].Value.ToString();
            PhoneNumberTb.Text = WarrantyDGV.SelectedRows[0].Cells[2].Value.ToString();
            GenCb.Text = WarrantyDGV.SelectedRows[0].Cells[3].Value.ToString();
            WarrentyTb.Text = WarrantyDGV.SelectedRows[0].Cells[4].Value.ToString();
            StatusCb.Text = WarrantyDGV.SelectedRows[0].Cells[5].Value.ToString();
            SDateTb.Value = Convert.ToDateTime(WarrantyDGV.SelectedRows[0].Cells[6].Value.ToString());
            EDateTb.Value = Convert.ToDateTime(WarrantyDGV.SelectedRows[0].Cells[7].Value.ToString());
            DetailsTb.Text = WarrantyDGV.SelectedRows[0].Cells[8].Value.ToString();

        }

        private void UpdateBtn_Click(object sender, EventArgs e)
        {
            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || GenCb.Text == "" || WarrentyTb.Text == "" || DetailsTb.Text == "")
            {
                MessageBox.Show("Enter The Warranty Details");
            }
            else
            {
                try
                {
                    int ID = Convert.ToInt32(WarrantyDGV.SelectedRows[0].Cells[0].Value.ToString());
                    string Name = NameTb.Text;
                    string Phone = PhoneNumberTb.Text;
                    string Gen = GenCb.Text;
                    string Warrenty = WarrentyTb.Text;
                    string Details = DetailsTb.Text;
                    string Sta = StatusCb.Text;
                    string Query = "UPDATE WarrantyTbl SET CustomerName = '{0}',  PhoneNumber = '{1}', Gender = '{2}', WarrantyType = '{3}', Status = '{4}', StartDate = '{5}',EndDate = '{6}', CarDetails = '{7}' WHERE Id = {8}";
                    Query = string.Format(Query, Name, Phone, Gen, Warrenty, Sta, SDateTb.Value.Date.ToString("yyyy-MM-dd"), EDateTb.Value.Date.ToString("yyyy-MM-dd"), Details,ID);
                    Con.setData(Query);
                    MessageBox.Show("Warranty Updated Successfully");
                    ShowWarranty();
                    NameTb.Text = "";
                    PhoneNumberTb.Text = "";
                    GenCb.Text = "";
                    WarrentyTb.Text = "";
                    DetailsTb.Text = "";
                    StatusCb.Text = "";

                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error in adding Warranty: " + ex.Message);
                }
            }

        }

        private void WDeleteBtn_Click(object sender, EventArgs e)
        {
            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || GenCb.Text == "" || WarrentyTb.Text == "" || DetailsTb.Text == "")
            {
                MessageBox.Show("Enter The Warranty Details");
            }
            else
            {
                try
                {
                    int ID = Convert.ToInt32(WarrantyDGV.SelectedRows[0].Cells[0].Value.ToString());
                    string Name = NameTb.Text;
                    string Phone = PhoneNumberTb.Text;
                    string Gen = GenCb.Text;
                    string Warrenty = WarrentyTb.Text;
                    string Details = DetailsTb.Text;
                    string Sta = StatusCb.Text;
                    string Query = "Delete from WarrantyTbl WHERE Id = {0}";
                    Query = string.Format(Query, ID);
                    Con.setData(Query);
                    MessageBox.Show("Warranty Deleted Successfully");
                    ShowWarranty();
                    NameTb.Text = "";
                    PhoneNumberTb.Text = "";
                    GenCb.Text = "";
                    WarrentyTb.Text = "";
                    DetailsTb.Text = "";
                    StatusCb.Text = "";

                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error in adding Warranty: " + ex.Message);
                }
            }

        }

        private void ManuBtn_Click_1(object sender, EventArgs e)
        {
            Dashboard dashboard = new Dashboard();
            dashboard.Show();
            this.Hide();

        }
    }
}
