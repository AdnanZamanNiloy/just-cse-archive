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
    public partial class Repair : Form
    {
        public Repair()
        {
            InitializeComponent();
            Con = new Functions();
            ShowRepair();
            RepairDGV.SelectionMode = DataGridViewSelectionMode.FullRowSelect;


        }
        Functions Con;
        private void ShowRepair()
        {
            try
            {
                RepairDGV.DataSource = null;
                String Query = "select * from RepairTbl";
                RepairDGV.DataSource = Con.getData(Query);
                RepairDGV.Refresh();

            }
            catch (Exception ex)
            {
                MessageBox.Show("Error in loading data: " + ex.Message);
            }
        }

        private void AddBtn_Click(object sender, EventArgs e)
        {
            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || CarNumTb.Text == "" || CarMoTb.Text == " " || DetailsTb.Text == " " || StatusCb.Text == " " || CostTb.Text == " ")
            {
                MessageBox.Show("Enter The Customer Details");
            }
            else
            {
                try
                {
                    string Name = NameTb.Text;
                    string Phone = PhoneNumberTb.Text;
                    string CarNum = CarNumTb.Text;
                    string CarModel = CarMoTb.Text;
                    string Details = DetailsTb.Text;
                    string RepairStatus = StatusCb.Text;
                    string Cost = CostTb.Text;
                    string Query = "insert into RepairTbl values('{0}', '{1}', '{2}', '{3}', '{4}', '{5}','{6}','{7}')";
                    Query = string.Format(Query, Name, Phone, CarNum, CarModel, Details, RepairStatus, RDateTb.Value.Date.ToString("yyyy-MM-dd"), Cost);
                    Con.setData(Query);
                    MessageBox.Show("Repair Details Added Successfully");
                    ShowRepair();
                    NameTb.Text = "";
                    PhoneNumberTb.Text = "";
                    CarNumTb.Text = "";
                    CarMoTb.Text = "";
                    DetailsTb.Text = "";
                    StatusCb.Text = "";
                    CostTb.Text = "";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error: " + ex.Message);
                }
            }
        }

        private void RepairDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            NameTb.Text = RepairDGV.SelectedRows[0].Cells[1].Value.ToString();
            PhoneNumberTb.Text = RepairDGV.SelectedRows[0].Cells[2].Value.ToString();
            CarNumTb.Text = RepairDGV.SelectedRows[0].Cells[3].Value.ToString();
            CarMoTb.Text = RepairDGV.SelectedRows[0].Cells[4].Value.ToString();
            DetailsTb.Text = RepairDGV.SelectedRows[0].Cells[5].Value.ToString();
            StatusCb.Text = RepairDGV.SelectedRows[0].Cells[6].Value.ToString();
            RDateTb.Text = RepairDGV.SelectedRows[0].Cells[7].Value.ToString();
            CostTb.Text = RepairDGV.SelectedRows[0].Cells[8].Value.ToString();
        }

        private void UpdateBtn_Click(object sender, EventArgs e)
        {
            if (NameTb.Text == "" || PhoneNumberTb.Text == "" || CarNumTb.Text == "" || CarMoTb.Text == " " || DetailsTb.Text == " " || StatusCb.Text == " " || CostTb.Text == " ")
            {
                MessageBox.Show("Enter The Customer Details");
            }
            else
            {
                try
                {
                    int RecordId = Convert.ToInt32(RepairDGV.SelectedRows[0].Cells[0].Value.ToString());
                    string Name = NameTb.Text;
                    string Phone = PhoneNumberTb.Text;
                    string CarNum = CarNumTb.Text;
                    string CarModel = CarMoTb.Text;
                    string Details = DetailsTb.Text;
                    string RepairStatus = StatusCb.Text;
                    string Cost = CostTb.Text;
                    string Query = "update RepairTbl set CustomerName = '{0}', CustomerContact = '{1}', CarNumber = '{2}', CarModel = '{3}', IssueDescription = '{4}', RepairStatus = '{5}', RepairDate = '{6}', Cost = '{7}' where RecordId = {8}";
                    Query = string.Format(Query, Name, Phone, CarNum, CarModel, Details, RepairStatus, RDateTb.Value.Date.ToString("yyyy-MM-dd"), Cost, RecordId);
                    Con.setData(Query);
                    MessageBox.Show("Repair Details Updated Successfully");
                    ShowRepair();
                    NameTb.Text = "";
                    PhoneNumberTb.Text = "";
                    CarNumTb.Text = "";
                    CarMoTb.Text = "";
                    DetailsTb.Text = "";
                    StatusCb.Text = "";
                    CostTb.Text = "";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error: " + ex.Message);
                }
            }
        }

        private void WDeleteBtn_Click(object sender, EventArgs e)
        {
            if (RepairDGV.SelectedRows.Count == 0)
            {
                MessageBox.Show("Select a record to delete.");
                return;
            }

            try
            {
                int RecordId = Convert.ToInt32(RepairDGV.SelectedRows[0].Cells[0].Value.ToString());
                string Query = "Delete from RepairTbl where RecordId = {0}";
                Query = string.Format(Query, RecordId);
                Con.setData(Query);
                MessageBox.Show("Repair Details Deleted Successfully");
                ShowRepair();
                NameTb.Text = "";
                PhoneNumberTb.Text = "";
                CarNumTb.Text = "";
                CarMoTb.Text = "";
                DetailsTb.Text = "";
                StatusCb.Text = "";
                CostTb.Text = "";
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
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
