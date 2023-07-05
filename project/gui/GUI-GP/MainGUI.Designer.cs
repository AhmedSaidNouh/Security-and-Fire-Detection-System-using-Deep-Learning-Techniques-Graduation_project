namespace GUI_GP
{
    partial class MainGUI
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
            this.uploadBut = new System.Windows.Forms.Button();
            this.realTimeBtn = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // uploadBut
            // 
            this.uploadBut.BackColor = System.Drawing.SystemColors.HotTrack;
            this.uploadBut.FlatAppearance.BorderSize = 0;
            this.uploadBut.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.uploadBut.Font = new System.Drawing.Font("DIN Next LT Arabic Medium", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.uploadBut.ForeColor = System.Drawing.Color.White;
            this.uploadBut.Location = new System.Drawing.Point(156, 446);
            this.uploadBut.Margin = new System.Windows.Forms.Padding(4, 4, 4, 4);
            this.uploadBut.Name = "uploadBut";
            this.uploadBut.Size = new System.Drawing.Size(247, 46);
            this.uploadBut.TabIndex = 0;
            this.uploadBut.Text = "UPLOAD YOUR VIDEO";
            this.uploadBut.UseVisualStyleBackColor = false;
            this.uploadBut.Click += new System.EventHandler(this.uploadBut_Click);
            // 
            // realTimeBtn
            // 
            this.realTimeBtn.BackColor = System.Drawing.SystemColors.HotTrack;
            this.realTimeBtn.FlatAppearance.BorderSize = 0;
            this.realTimeBtn.FlatStyle = System.Windows.Forms.FlatStyle.Flat;
            this.realTimeBtn.Font = new System.Drawing.Font("DIN Next LT Arabic Medium", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.realTimeBtn.ForeColor = System.Drawing.Color.White;
            this.realTimeBtn.Location = new System.Drawing.Point(156, 500);
            this.realTimeBtn.Margin = new System.Windows.Forms.Padding(4);
            this.realTimeBtn.Name = "realTimeBtn";
            this.realTimeBtn.Size = new System.Drawing.Size(247, 46);
            this.realTimeBtn.TabIndex = 1;
            this.realTimeBtn.Text = "REAL TIME DETECTION";
            this.realTimeBtn.UseVisualStyleBackColor = false;
            this.realTimeBtn.Click += new System.EventHandler(this.realTimeBtn_Click);
            // 
            // MainGUI
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::GUI_GP.Properties.Resources.interface_GP;
            this.ClientSize = new System.Drawing.Size(1069, 742);
            this.Controls.Add(this.realTimeBtn);
            this.Controls.Add(this.uploadBut);
            this.Margin = new System.Windows.Forms.Padding(3, 2, 3, 2);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1087, 789);
            this.MinimumSize = new System.Drawing.Size(1087, 789);
            this.Name = "MainGUI";
            this.RightToLeft = System.Windows.Forms.RightToLeft.No;
            this.Text = "SECURITY SYSTEM & FIRE DETECTION - GUI";
            this.Load += new System.EventHandler(this.Form1_Load);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button uploadBut;
        private System.Windows.Forms.Button realTimeBtn;
    }
}

