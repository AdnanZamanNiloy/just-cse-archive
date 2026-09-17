using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Drawing.Printing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace CarShowRm
{
    public partial class Bill : Form
    {
        public Bill()
        {
            InitializeComponent();
            Con = new Functions();
            ShowCars();
            AVCDGV.SelectionMode = DataGridViewSelectionMode.FullRowSelect;
        }
        Functions Con;
        private void ShowCars()
        {
            try
            {
                AVCDGV.DataSource = null;
                string Query = "select * from CarsTbl";
                AVCDGV.DataSource = Con.getData(Query);
                AVCDGV.Refresh();
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error in loading data: " + ex.Message);
            }
        }
        private void AVCDGV_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            CarNumber.Text = AVCDGV.SelectedRows[0].Cells[0].Value.ToString();
            CarModel.Text = AVCDGV.SelectedRows[0].Cells[6].Value.ToString();
            CarMn.Text = AVCDGV.SelectedRows[0].Cells[1].Value.ToString();
            CarPrice.Text = AVCDGV.SelectedRows[0].Cells[4].Value.ToString();
            CarDescription.Text = AVCDGV.SelectedRows[0].Cells[5].Value.ToString();

            // Trigger the Total_TextChanged event to update the total
            Total_TextChanged(sender, e);
        }

        private void PrintBtn_Click(object sender, EventArgs e)
        {
            MprintDocument.Print();
        }

        private void PreviewBtn_Click(object sender, EventArgs e)
        {
            MprintPreviewDialog.Document = MprintDocument;
            MprintPreviewDialog.ShowDialog();
        }

        private void ResetBtn_Click(object sender, EventArgs e)
        {
            CusName.Text = "";
            CusAddress.Text = "";
            CarNumber.Text = "";
            CarMn.Text = "";
            CarPrice.Text = "";
            CarDescription.Text = "";
            Others.Text = "";
            Total.Text = "";
        }

        private void MprintDocument_PrintPage(object sender, PrintPageEventArgs e)
        {
            Bitmap bmp = Properties.Resources.car_logo_vector;
            Image newimage = bmp;
            float x = (e.PageBounds.Width - newimage.Width / 2) / 2;
            float y = 15;
            float newWidth = newimage.Width / 2;
            float newHeight = newimage.Height / 2;

            e.Graphics.DrawImage(newimage, x, y, newWidth, newHeight);

            // Print the Car Showroom Management System details
            string header = "Car Showroom Management System";
            string contact = "Contact No.: 01752698564";
            string location = "Location: Dhaka, Bangladesh";

            Font headerFont = new Font("Arial", 16, FontStyle.Bold);
            Font detailsFont = new Font("Arial", 12, FontStyle.Regular);
            Font thankYouFont = new Font("Arial", 14, FontStyle.Bold); // Increased font size for thank you message

            float headerX = e.MarginBounds.Left;
            float headerY = y + newHeight + 20; // Adjust the Y position below the image

            string Dashline = "----------------------------------------------------------------------------------------------------------";

            e.Graphics.DrawString(header, headerFont, Brushes.Black, headerX, headerY);
            e.Graphics.DrawString(contact, detailsFont, Brushes.Black, headerX, headerY + 30);
            e.Graphics.DrawString(location, detailsFont, Brushes.Black, headerX, headerY + 50);
            e.Graphics.DrawString("Date: " + DateTime.Now.ToString(), detailsFont, Brushes.Black, headerX, headerY + 70);
            e.Graphics.DrawString(Dashline, detailsFont, Brushes.Black, headerX, headerY + 90);
            e.Graphics.DrawString("Customer Name: " + CusName.Text, detailsFont, Brushes.Black, headerX, headerY + 130);
            e.Graphics.DrawString("Customer Address: " + CusAddress.Text, detailsFont, Brushes.Black, headerX, headerY + 160);
            e.Graphics.DrawString("Car Number: " + CarNumber.Text, detailsFont, Brushes.Black, headerX, headerY + 190);
            e.Graphics.DrawString("Car Model: " + CarModel.Text, detailsFont, Brushes.Black, headerX, headerY + 220);
            e.Graphics.DrawString("Manufacturer: " + CarMn.Text, detailsFont, Brushes.Black, headerX, headerY + 250);
            e.Graphics.DrawString("Price(TK): " + CarPrice.Text, detailsFont, Brushes.Black, headerX, headerY + 280);
            e.Graphics.DrawString("Car Description: " + CarDescription.Text, detailsFont, Brushes.Black, headerX, headerY + 310);
            e.Graphics.DrawString("Others Cost(TK): " + Others.Text, detailsFont, Brushes.Black, headerX, headerY + 340);
            e.Graphics.DrawString("Total Amount(TK): " + Total.Text, detailsFont, Brushes.Black, headerX, headerY + 370);
            e.Graphics.DrawString(Dashline, detailsFont, Brushes.Black, headerX, headerY + 400);
            e.Graphics.DrawString("Thank you for visiting us!", thankYouFont, Brushes.Black, headerX, headerY + 440); // Increased font size
            e.Graphics.DrawString(Dashline, detailsFont, Brushes.Black, headerX, headerY + 470);
            e.Graphics.DrawString("Developed by: Adnan Zaman", detailsFont, Brushes.Black, headerX, headerY + 720);

            // Add Manager's and Buyer's signatures
            float managerSignatureX = e.MarginBounds.Left;
            float buyerSignatureX = e.MarginBounds.Right - 200; // Adjust the X position to the right side
            float signatureY = headerY + 600; // Adjust the Y position as needed

            e.Graphics.DrawString("Manager Signature: _______________", detailsFont, Brushes.Black, managerSignatureX, signatureY);
            e.Graphics.DrawString("Buyer's Signature: _______________", detailsFont, Brushes.Black, buyerSignatureX, signatureY);
        }

        private void button3_Click(object sender, EventArgs e)
        {
            Dashboard ds = new Dashboard();
            ds.Show();
            this.Hide();
        }

        private void Total_TextChanged(object sender, EventArgs e)
        {
            if (string.IsNullOrEmpty(Others.Text))
            {
                Others.Text = "0";
            }

            if (int.TryParse(CarPrice.Text, out int carPriceValue) && int.TryParse(Others.Text, out int othersValue))
            {
                int total = carPriceValue + othersValue;
                Total.Text = total.ToString();
            }
            else
            {

                Total.Text = CarPrice.Text;
            }
        }
    }
}
