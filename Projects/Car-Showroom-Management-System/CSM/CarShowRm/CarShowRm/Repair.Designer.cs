namespace CarShowRm
{
    partial class Repair
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(Repair));
            this.pictureBox2 = new System.Windows.Forms.PictureBox();
            this.label1 = new System.Windows.Forms.Label();
            this.AddBtn = new System.Windows.Forms.Button();
            this.label2 = new System.Windows.Forms.Label();
            this.StatusCb = new System.Windows.Forms.ComboBox();
            this.RepairStatusCb = new System.Windows.Forms.Label();
            this.DescriptionTb = new System.Windows.Forms.Label();
            this.CostTb = new System.Windows.Forms.TextBox();
            this.Rb = new System.Windows.Forms.Label();
            this.RDateTb = new System.Windows.Forms.DateTimePicker();
            this.DeleteBtn = new System.Windows.Forms.Button();
            this.panel2 = new System.Windows.Forms.Panel();
            this.UpdateBtn = new System.Windows.Forms.Button();
            this.WDeleteBtn = new System.Windows.Forms.Button();
            this.pictureBox8 = new System.Windows.Forms.PictureBox();
            this.button4 = new System.Windows.Forms.Button();
            this.panel3 = new System.Windows.Forms.Panel();
            this.Cost = new System.Windows.Forms.Label();
            this.CarMoTb = new System.Windows.Forms.TextBox();
            this.CarNumTb = new System.Windows.Forms.TextBox();
            this.CarModelTb = new System.Windows.Forms.Label();
            this.CarNumberTb = new System.Windows.Forms.Label();
            this.PhoneNumTb = new System.Windows.Forms.Label();
            this.CustomerNameTb = new System.Windows.Forms.Label();
            this.DetailsTb = new System.Windows.Forms.TextBox();
            this.PhoneNumberTb = new System.Windows.Forms.TextBox();
            this.NameTb = new System.Windows.Forms.TextBox();
            this.panel4 = new System.Windows.Forms.Panel();
            this.ManuBtn = new System.Windows.Forms.Button();
            this.RepairDGV = new System.Windows.Forms.DataGridView();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).BeginInit();
            this.panel2.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox8)).BeginInit();
            this.panel3.SuspendLayout();
            this.panel4.SuspendLayout();
            ((System.ComponentModel.ISupportInitialize)(this.RepairDGV)).BeginInit();
            this.SuspendLayout();
            // 
            // pictureBox2
            // 
            this.pictureBox2.BackColor = System.Drawing.Color.Transparent;
            this.pictureBox2.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox2.Image")));
            this.pictureBox2.Location = new System.Drawing.Point(27, -2);
            this.pictureBox2.Name = "pictureBox2";
            this.pictureBox2.Size = new System.Drawing.Size(70, 29);
            this.pictureBox2.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox2.TabIndex = 29;
            this.pictureBox2.TabStop = false;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.BackColor = System.Drawing.Color.White;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.ForeColor = System.Drawing.Color.DarkBlue;
            this.label1.Location = new System.Drawing.Point(574, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(364, 25);
            this.label1.TabIndex = 31;
            this.label1.Text = "Car Showroom Management System";
            // 
            // AddBtn
            // 
            this.AddBtn.BackColor = System.Drawing.Color.DarkBlue;
            this.AddBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.AddBtn.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.AddBtn.Location = new System.Drawing.Point(69, 240);
            this.AddBtn.Name = "AddBtn";
            this.AddBtn.Size = new System.Drawing.Size(155, 37);
            this.AddBtn.TabIndex = 14;
            this.AddBtn.Text = "Save Record";
            this.AddBtn.UseVisualStyleBackColor = false;
            this.AddBtn.Click += new System.EventHandler(this.AddBtn_Click);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.ForeColor = System.Drawing.Color.AliceBlue;
            this.label2.Location = new System.Drawing.Point(444, 10);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(84, 25);
            this.label2.TabIndex = 0;
            this.label2.Text = "Details ";
            // 
            // StatusCb
            // 
            this.StatusCb.FormattingEnabled = true;
            this.StatusCb.Items.AddRange(new object[] {
            "Pending",
            "Completed",
            "Not Started"});
            this.StatusCb.Location = new System.Drawing.Point(749, 169);
            this.StatusCb.Name = "StatusCb";
            this.StatusCb.Size = new System.Drawing.Size(217, 24);
            this.StatusCb.TabIndex = 23;
            // 
            // RepairStatusCb
            // 
            this.RepairStatusCb.AutoSize = true;
            this.RepairStatusCb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RepairStatusCb.Location = new System.Drawing.Point(552, 169);
            this.RepairStatusCb.Name = "RepairStatusCb";
            this.RepairStatusCb.Size = new System.Drawing.Size(111, 20);
            this.RepairStatusCb.TabIndex = 22;
            this.RepairStatusCb.Text = "Repair Status";
            // 
            // DescriptionTb
            // 
            this.DescriptionTb.AutoSize = true;
            this.DescriptionTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DescriptionTb.Location = new System.Drawing.Point(552, 82);
            this.DescriptionTb.Name = "DescriptionTb";
            this.DescriptionTb.Size = new System.Drawing.Size(140, 20);
            this.DescriptionTb.TabIndex = 21;
            this.DescriptionTb.Text = "Issue Description";
            // 
            // CostTb
            // 
            this.CostTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CostTb.Location = new System.Drawing.Point(749, 221);
            this.CostTb.Name = "CostTb";
            this.CostTb.Size = new System.Drawing.Size(217, 27);
            this.CostTb.TabIndex = 20;
            // 
            // Rb
            // 
            this.Rb.AutoSize = true;
            this.Rb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Rb.Location = new System.Drawing.Point(48, 327);
            this.Rb.Name = "Rb";
            this.Rb.Size = new System.Drawing.Size(99, 20);
            this.Rb.TabIndex = 19;
            this.Rb.Text = "Repair Date";
            // 
            // RDateTb
            // 
            this.RDateTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.RDateTb.Location = new System.Drawing.Point(201, 320);
            this.RDateTb.Name = "RDateTb";
            this.RDateTb.Size = new System.Drawing.Size(217, 27);
            this.RDateTb.TabIndex = 18;
            // 
            // DeleteBtn
            // 
            this.DeleteBtn.BackColor = System.Drawing.Color.DarkBlue;
            this.DeleteBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DeleteBtn.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.DeleteBtn.Location = new System.Drawing.Point(52, 411);
            this.DeleteBtn.Name = "DeleteBtn";
            this.DeleteBtn.Size = new System.Drawing.Size(336, 39);
            this.DeleteBtn.TabIndex = 16;
            this.DeleteBtn.Text = "Delete Customer";
            this.DeleteBtn.UseVisualStyleBackColor = false;
            // 
            // panel2
            // 
            this.panel2.BackColor = System.Drawing.Color.White;
            this.panel2.Controls.Add(this.UpdateBtn);
            this.panel2.Controls.Add(this.WDeleteBtn);
            this.panel2.Controls.Add(this.pictureBox8);
            this.panel2.Controls.Add(this.button4);
            this.panel2.Controls.Add(this.panel3);
            this.panel2.Controls.Add(this.AddBtn);
            this.panel2.Location = new System.Drawing.Point(3, 28);
            this.panel2.Name = "panel2";
            this.panel2.Size = new System.Drawing.Size(1373, 412);
            this.panel2.TabIndex = 30;
            // 
            // UpdateBtn
            // 
            this.UpdateBtn.BackColor = System.Drawing.Color.DarkBlue;
            this.UpdateBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.UpdateBtn.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.UpdateBtn.Location = new System.Drawing.Point(69, 290);
            this.UpdateBtn.Name = "UpdateBtn";
            this.UpdateBtn.Size = new System.Drawing.Size(155, 37);
            this.UpdateBtn.TabIndex = 27;
            this.UpdateBtn.Text = "Update Record";
            this.UpdateBtn.UseVisualStyleBackColor = false;
            this.UpdateBtn.Click += new System.EventHandler(this.UpdateBtn_Click);
            // 
            // WDeleteBtn
            // 
            this.WDeleteBtn.BackColor = System.Drawing.Color.DarkBlue;
            this.WDeleteBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.WDeleteBtn.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.WDeleteBtn.Location = new System.Drawing.Point(69, 342);
            this.WDeleteBtn.Name = "WDeleteBtn";
            this.WDeleteBtn.Size = new System.Drawing.Size(155, 37);
            this.WDeleteBtn.TabIndex = 26;
            this.WDeleteBtn.Text = "Delete Record";
            this.WDeleteBtn.UseVisualStyleBackColor = false;
            this.WDeleteBtn.Click += new System.EventHandler(this.WDeleteBtn_Click);
            // 
            // pictureBox8
            // 
            this.pictureBox8.Image = ((System.Drawing.Image)(resources.GetObject("pictureBox8.Image")));
            this.pictureBox8.Location = new System.Drawing.Point(3, 45);
            this.pictureBox8.Name = "pictureBox8";
            this.pictureBox8.Size = new System.Drawing.Size(323, 178);
            this.pictureBox8.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pictureBox8.TabIndex = 16;
            this.pictureBox8.TabStop = false;
            // 
            // button4
            // 
            this.button4.BackColor = System.Drawing.Color.DarkBlue;
            this.button4.Font = new System.Drawing.Font("Microsoft Sans Serif", 12F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.button4.ForeColor = System.Drawing.SystemColors.ButtonHighlight;
            this.button4.Location = new System.Drawing.Point(-7, 0);
            this.button4.Name = "button4";
            this.button4.Size = new System.Drawing.Size(1377, 39);
            this.button4.TabIndex = 15;
            this.button4.Text = "Repair and Maintenance Module";
            this.button4.UseVisualStyleBackColor = false;
            // 
            // panel3
            // 
            this.panel3.BackColor = System.Drawing.Color.White;
            this.panel3.Controls.Add(this.Cost);
            this.panel3.Controls.Add(this.CarMoTb);
            this.panel3.Controls.Add(this.CarNumTb);
            this.panel3.Controls.Add(this.StatusCb);
            this.panel3.Controls.Add(this.RepairStatusCb);
            this.panel3.Controls.Add(this.DescriptionTb);
            this.panel3.Controls.Add(this.CostTb);
            this.panel3.Controls.Add(this.Rb);
            this.panel3.Controls.Add(this.RDateTb);
            this.panel3.Controls.Add(this.DeleteBtn);
            this.panel3.Controls.Add(this.CarModelTb);
            this.panel3.Controls.Add(this.CarNumberTb);
            this.panel3.Controls.Add(this.PhoneNumTb);
            this.panel3.Controls.Add(this.CustomerNameTb);
            this.panel3.Controls.Add(this.DetailsTb);
            this.panel3.Controls.Add(this.PhoneNumberTb);
            this.panel3.Controls.Add(this.NameTb);
            this.panel3.Controls.Add(this.panel4);
            this.panel3.Location = new System.Drawing.Point(332, 45);
            this.panel3.Name = "panel3";
            this.panel3.Size = new System.Drawing.Size(1038, 365);
            this.panel3.TabIndex = 25;
            // 
            // Cost
            // 
            this.Cost.AutoSize = true;
            this.Cost.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.Cost.Location = new System.Drawing.Point(552, 228);
            this.Cost.Name = "Cost";
            this.Cost.Size = new System.Drawing.Size(44, 20);
            this.Cost.TabIndex = 27;
            this.Cost.Text = "Cost";
            // 
            // CarMoTb
            // 
            this.CarMoTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CarMoTb.Location = new System.Drawing.Point(201, 265);
            this.CarMoTb.Name = "CarMoTb";
            this.CarMoTb.Size = new System.Drawing.Size(217, 27);
            this.CarMoTb.TabIndex = 25;
            // 
            // CarNumTb
            // 
            this.CarNumTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CarNumTb.Location = new System.Drawing.Point(201, 198);
            this.CarNumTb.Name = "CarNumTb";
            this.CarNumTb.Size = new System.Drawing.Size(217, 27);
            this.CarNumTb.TabIndex = 24;
            // 
            // CarModelTb
            // 
            this.CarModelTb.AutoSize = true;
            this.CarModelTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CarModelTb.Location = new System.Drawing.Point(48, 268);
            this.CarModelTb.Name = "CarModelTb";
            this.CarModelTb.Size = new System.Drawing.Size(86, 20);
            this.CarModelTb.TabIndex = 11;
            this.CarModelTb.Text = "Car Model";
            // 
            // CarNumberTb
            // 
            this.CarNumberTb.AutoSize = true;
            this.CarNumberTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CarNumberTb.Location = new System.Drawing.Point(48, 205);
            this.CarNumberTb.Name = "CarNumberTb";
            this.CarNumberTb.Size = new System.Drawing.Size(100, 20);
            this.CarNumberTb.TabIndex = 9;
            this.CarNumberTb.Text = "Car Number";
            // 
            // PhoneNumTb
            // 
            this.PhoneNumTb.AutoSize = true;
            this.PhoneNumTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PhoneNumTb.Location = new System.Drawing.Point(48, 142);
            this.PhoneNumTb.Name = "PhoneNumTb";
            this.PhoneNumTb.Size = new System.Drawing.Size(131, 20);
            this.PhoneNumTb.TabIndex = 8;
            this.PhoneNumTb.Text = "Contact Number";
            // 
            // CustomerNameTb
            // 
            this.CustomerNameTb.AutoSize = true;
            this.CustomerNameTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.CustomerNameTb.Location = new System.Drawing.Point(48, 75);
            this.CustomerNameTb.Name = "CustomerNameTb";
            this.CustomerNameTb.Size = new System.Drawing.Size(92, 20);
            this.CustomerNameTb.TabIndex = 6;
            this.CustomerNameTb.Text = "Cus. Name";
            // 
            // DetailsTb
            // 
            this.DetailsTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.DetailsTb.Location = new System.Drawing.Point(749, 68);
            this.DetailsTb.Multiline = true;
            this.DetailsTb.Name = "DetailsTb";
            this.DetailsTb.Size = new System.Drawing.Size(217, 61);
            this.DetailsTb.TabIndex = 4;
            // 
            // PhoneNumberTb
            // 
            this.PhoneNumberTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.PhoneNumberTb.Location = new System.Drawing.Point(201, 135);
            this.PhoneNumberTb.Name = "PhoneNumberTb";
            this.PhoneNumberTb.Size = new System.Drawing.Size(217, 27);
            this.PhoneNumberTb.TabIndex = 3;
            // 
            // NameTb
            // 
            this.NameTb.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.NameTb.Location = new System.Drawing.Point(201, 68);
            this.NameTb.Name = "NameTb";
            this.NameTb.Size = new System.Drawing.Size(217, 27);
            this.NameTb.TabIndex = 2;
            // 
            // panel4
            // 
            this.panel4.BackColor = System.Drawing.Color.DarkBlue;
            this.panel4.Controls.Add(this.label2);
            this.panel4.Location = new System.Drawing.Point(3, 3);
            this.panel4.Name = "panel4";
            this.panel4.Size = new System.Drawing.Size(1031, 44);
            this.panel4.TabIndex = 1;
            // 
            // ManuBtn
            // 
            this.ManuBtn.Font = new System.Drawing.Font("Microsoft Sans Serif", 10.2F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.ManuBtn.ForeColor = System.Drawing.Color.Blue;
            this.ManuBtn.Location = new System.Drawing.Point(81, -2);
            this.ManuBtn.Name = "ManuBtn";
            this.ManuBtn.Size = new System.Drawing.Size(75, 32);
            this.ManuBtn.TabIndex = 33;
            this.ManuBtn.Text = "Manu";
            this.ManuBtn.UseVisualStyleBackColor = true;
            this.ManuBtn.Click += new System.EventHandler(this.ManuBtn_Click);
            // 
            // RepairDGV
            // 
            this.RepairDGV.BackgroundColor = System.Drawing.Color.White;
            this.RepairDGV.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.RepairDGV.Location = new System.Drawing.Point(3, 444);
            this.RepairDGV.Name = "RepairDGV";
            this.RepairDGV.RowHeadersWidth = 51;
            this.RepairDGV.RowTemplate.Height = 24;
            this.RepairDGV.Size = new System.Drawing.Size(1366, 272);
            this.RepairDGV.TabIndex = 34;
            this.RepairDGV.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.RepairDGV_CellContentClick);
            // 
            // Repair
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackColor = System.Drawing.Color.White;
            this.ClientSize = new System.Drawing.Size(1375, 721);
            this.Controls.Add(this.RepairDGV);
            this.Controls.Add(this.ManuBtn);
            this.Controls.Add(this.pictureBox2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.panel2);
            this.Name = "Repair";
            this.Text = "Repair";
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox2)).EndInit();
            this.panel2.ResumeLayout(false);
            ((System.ComponentModel.ISupportInitialize)(this.pictureBox8)).EndInit();
            this.panel3.ResumeLayout(false);
            this.panel3.PerformLayout();
            this.panel4.ResumeLayout(false);
            this.panel4.PerformLayout();
            ((System.ComponentModel.ISupportInitialize)(this.RepairDGV)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pictureBox2;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button AddBtn;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox StatusCb;
        private System.Windows.Forms.Label RepairStatusCb;
        private System.Windows.Forms.Label DescriptionTb;
        private System.Windows.Forms.TextBox CostTb;
        private System.Windows.Forms.Label Rb;
        private System.Windows.Forms.DateTimePicker RDateTb;
        private System.Windows.Forms.Button DeleteBtn;
        private System.Windows.Forms.Panel panel2;
        private System.Windows.Forms.Button UpdateBtn;
        private System.Windows.Forms.Button WDeleteBtn;
        private System.Windows.Forms.PictureBox pictureBox8;
        private System.Windows.Forms.Button button4;
        private System.Windows.Forms.Panel panel3;
        private System.Windows.Forms.Label CarModelTb;
        private System.Windows.Forms.Label CarNumberTb;
        private System.Windows.Forms.Label PhoneNumTb;
        private System.Windows.Forms.Label CustomerNameTb;
        private System.Windows.Forms.TextBox DetailsTb;
        private System.Windows.Forms.TextBox PhoneNumberTb;
        private System.Windows.Forms.TextBox NameTb;
        private System.Windows.Forms.Panel panel4;
        private System.Windows.Forms.TextBox CarMoTb;
        private System.Windows.Forms.TextBox CarNumTb;
        private System.Windows.Forms.Label Cost;
        private System.Windows.Forms.Button ManuBtn;
        private System.Windows.Forms.DataGridView RepairDGV;
    }
}