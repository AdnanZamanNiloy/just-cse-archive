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
    public partial class Cars : Form
    {
        public Cars()
        {
            InitializeComponent();
            Con = new Functions();
            ShowCars();
            CarsDGV.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
        }
        Functions Con;

        private void ShowCars()
        {
            try
            {
                CarsDGV.DataSource = null;
                string Query = "select * from CarsTbl";
                CarsDGV.DataSource = Con.getData(Query);
                CarsDGV.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error in loading data: " + ex.Message);
            }
        }

        private void AddBtn_Click(object sender, EventArgs e)
        {
            if (CNumberTb.Text == "" || ColorTb.Text == "" || Price.Text == "" || DescriptionTb.Text == "" || ManTb.Text == "" || ModelTb.Text == "" || EngineTb.Text == "")
            {
                MessageBox.Show("Enter The Car Details");
            }
            else
            {
                try
                {
                    string CNumber = CNumberTb.Text;
                    string Manufacturer = ManTb.Text;
                    string Color = ColorTb.Text;
                    int Price = Convert.ToInt32(this.Price.Text);
                    string Desc = DescriptionTb.Text;
                    string CarModel = ModelTb.Text;
                    string EngineType = EngineTb.Text;
                    string Query = "INSERT INTO CarsTbl VALUES ('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')";
                    Query = string.Format(Query, CNumber, Manufacturer, Color, YearTb.Value.Date.ToString("yyyy-MM-dd"), Price, Desc, CarModel, EngineType);
                    Con.setData(Query);
                    MessageBox.Show("Car Registered Succesfully");
                    ShowCars();
                    CNumberTb.Text = "";
                    ManTb.Text = "";
                    ColorTb.Text = "";
                    this.Price.Text = "";
                    DescriptionTb.Text = "";
                    ModelTb.Text = "";
                    EngineTb.Text = "";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error in adding car: " + ex.Message);
                }
            }
        }

        private void CarsDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            CNumberTb.Text = CarsDGV.SelectedRows[0].Cells[0].Value.ToString();
            ManTb.Text = CarsDGV.SelectedRows[0].Cells[1].Value.ToString();
            ColorTb.Text = CarsDGV.SelectedRows[0].Cells[2].Value.ToString();
            YearTb.Value = Convert.ToDateTime(CarsDGV.SelectedRows[0].Cells[3].Value.ToString());
            Price.Text = CarsDGV.SelectedRows[0].Cells[4].Value.ToString();
            DescriptionTb.Text = CarsDGV.SelectedRows[0].Cells[5].Value.ToString();
            ModelTb.Text = CarsDGV.SelectedRows[0].Cells[6].Value.ToString();
            EngineTb.Text = CarsDGV.SelectedRows[0].Cells[7].Value.ToString();
        }

        private void EditBtn_Click(object sender, EventArgs e)
        {
            if (CNumberTb.Text == "" || ColorTb.Text == "" || Price.Text == "" || DescriptionTb.Text == "" || ManTb.Text == "" || ModelTb.Text == "" || EngineTb.Text == "")
            {
                MessageBox.Show("Enter The Car Details");
            }
            else
            {
                try
                {
                    string CNumber = CNumberTb.Text;
                    string Manufacturer = ManTb.Text;
                    string Color = ColorTb.Text;
                    int Price = Convert.ToInt32(this.Price.Text);
                    string Desc = DescriptionTb.Text;
                    string CarModel = ModelTb.Text;
                    string EngineType = EngineTb.Text;
                    string Query = "UPDATE CarsTbl SET Manufacturer = '{1}', Color = '{2}', YearOfMn = '{3}', Price = '{4}', Description = '{5}', CarModel = '{6}', EngineType = '{7}' WHERE CNumber = '{0}'";
                    Query = string.Format(Query, CNumber, Manufacturer, Color, YearTb.Value.Date.ToString("yyyy-MM-dd"), Price, Desc, CarModel, EngineType);
                    Con.setData(Query);
                    MessageBox.Show("Car Info Update Succesfully");
                    ShowCars();
                    CNumberTb.Text = "";
                    ManTb.Text = "";
                    ColorTb.Text = "";
                    this.Price.Text = "";
                    DescriptionTb.Text = "";
                    ModelTb.Text = "";
                    EngineTb.Text = "";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error in updating car: " + ex.Message);
                }
            }
        }

        private void DeleteBtn_Click(object sender, EventArgs e)
        {
            if (CNumberTb.Text == "" || ColorTb.Text == "" || Price.Text == "" || DescriptionTb.Text == "" || ManTb.Text == "" || ModelTb.Text == "" || EngineTb.Text == "")
            {
                MessageBox.Show("Enter The Car Details");
            }
            else
            {
                try
                {
                    string CNumber = CNumberTb.Text;
                    string Query = "DELETE FROM CarsTbl WHERE CNumber = '{0}'";
                    Query = string.Format(Query, CNumber);
                    Con.setData(Query);
                    MessageBox.Show("Car Deleted Successfully");
                    ShowCars();
                    CNumberTb.Text = "";
                    ManTb.Text = "";
                    ColorTb.Text = "";
                    this.Price.Text = "";
                    DescriptionTb.Text = "";
                    ModelTb.Text = "";
                    EngineTb.Text = "";
                }
                catch (Exception ex)
                {
                    MessageBox.Show("Error in deleting car: " + ex.Message);
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

