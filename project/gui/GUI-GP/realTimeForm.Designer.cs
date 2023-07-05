namespace GUI_GP
{
    partial class realTimeForm
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
            this.fireRealTxt = new System.Windows.Forms.Label();
            this.weaponRealTxt = new System.Windows.Forms.Label();
            this.nameRealTxt = new System.Windows.Forms.Label();
            this.photoBox = new System.Windows.Forms.PictureBox();
            this.pic = new System.Windows.Forms.PictureBox();
            ((System.ComponentModel.ISupportInitialize)(this.photoBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic)).BeginInit();
            this.SuspendLayout();
            // 
            // fireRealTxt
            // 
            this.fireRealTxt.BackColor = System.Drawing.Color.Transparent;
            this.fireRealTxt.Font = new System.Drawing.Font("DIN Next LT Arabic", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fireRealTxt.ForeColor = System.Drawing.SystemColors.Desktop;
            this.fireRealTxt.Location = new System.Drawing.Point(383, 677);
            this.fireRealTxt.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.fireRealTxt.Name = "fireRealTxt";
            this.fireRealTxt.Size = new System.Drawing.Size(203, 30);
            this.fireRealTxt.TabIndex = 8;
            this.fireRealTxt.Text = "DEFAULT VALUE";
            // 
            // weaponRealTxt
            // 
            this.weaponRealTxt.BackColor = System.Drawing.Color.Transparent;
            this.weaponRealTxt.Font = new System.Drawing.Font("DIN Next LT Arabic", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.weaponRealTxt.ForeColor = System.Drawing.SystemColors.Desktop;
            this.weaponRealTxt.Location = new System.Drawing.Point(383, 626);
            this.weaponRealTxt.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.weaponRealTxt.Name = "weaponRealTxt";
            this.weaponRealTxt.Size = new System.Drawing.Size(203, 30);
            this.weaponRealTxt.TabIndex = 7;
            this.weaponRealTxt.Text = "DEFAULT VALUE";
            // 
            // nameRealTxt
            // 
            this.nameRealTxt.BackColor = System.Drawing.Color.Transparent;
            this.nameRealTxt.Font = new System.Drawing.Font("DIN Next LT Arabic", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.nameRealTxt.ForeColor = System.Drawing.SystemColors.Desktop;
            this.nameRealTxt.Location = new System.Drawing.Point(383, 578);
            this.nameRealTxt.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.nameRealTxt.Name = "nameRealTxt";
            this.nameRealTxt.Size = new System.Drawing.Size(203, 30);
            this.nameRealTxt.TabIndex = 6;
            this.nameRealTxt.Text = "DEFAULT VALUE";
            // 
            // photoBox
            // 
            this.photoBox.InitialImage = global::GUI_GP.Properties.Resources._179_1796406_thinking_man_download_transparent_png_image_man_thinking;
            this.photoBox.Location = new System.Drawing.Point(28, 583);
            this.photoBox.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.photoBox.Name = "photoBox";
            this.photoBox.Size = new System.Drawing.Size(144, 140);
            this.photoBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.photoBox.TabIndex = 5;
            this.photoBox.TabStop = false;
            this.photoBox.Click += new System.EventHandler(this.photoBox_Click);
            // 
            // pic
            // 
            this.pic.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pic.Location = new System.Drawing.Point(28, 233);
            this.pic.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.pic.Name = "pic";
            this.pic.Size = new System.Drawing.Size(562, 294);
            this.pic.SizeMode = System.Windows.Forms.PictureBoxSizeMode.Zoom;
            this.pic.TabIndex = 9;
            this.pic.TabStop = false;
            this.pic.Click += new System.EventHandler(this.pic_Click);
            // 
            // realTimeForm
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::GUI_GP.Properties.Resources.interface_21;
            this.ClientSize = new System.Drawing.Size(1063, 724);
            this.Controls.Add(this.pic);
            this.Controls.Add(this.fireRealTxt);
            this.Controls.Add(this.weaponRealTxt);
            this.Controls.Add(this.nameRealTxt);
            this.Controls.Add(this.photoBox);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1081, 771);
            this.MinimumSize = new System.Drawing.Size(1081, 771);
            this.Name = "realTimeForm";
            this.Text = "SECURITY SYSTEM & FIRE DETECTION - REALTIME VIDEO ";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.realTimeForm_FormClosing);
            this.Load += new System.EventHandler(this.realTimeForm_Load);
            ((System.ComponentModel.ISupportInitialize)(this.photoBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pic)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Label fireRealTxt;
        private System.Windows.Forms.Label weaponRealTxt;
        private System.Windows.Forms.Label nameRealTxt;
        private System.Windows.Forms.PictureBox photoBox;
        private System.Windows.Forms.PictureBox pic;
    }
}