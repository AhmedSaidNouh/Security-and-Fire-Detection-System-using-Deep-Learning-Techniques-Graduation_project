namespace GUI_GP
{
    partial class DisplayVideo
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
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(DisplayVideo));
            this.photoBox = new System.Windows.Forms.PictureBox();
            this.nameTxt = new System.Windows.Forms.Label();
            this.weaponTxt = new System.Windows.Forms.Label();
            this.fireTxt = new System.Windows.Forms.Label();
            this.videoPlayer = new AxWMPLib.AxWindowsMediaPlayer();
            ((System.ComponentModel.ISupportInitialize)(this.photoBox)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.videoPlayer)).BeginInit();
            this.SuspendLayout();
            // 
            // photoBox
            // 
            this.photoBox.InitialImage = global::GUI_GP.Properties.Resources._179_1796406_thinking_man_download_transparent_png_image_man_thinking;
            this.photoBox.Location = new System.Drawing.Point(32, 585);
            this.photoBox.Margin = new System.Windows.Forms.Padding(4);
            this.photoBox.Name = "photoBox";
            this.photoBox.Size = new System.Drawing.Size(144, 140);
            this.photoBox.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.photoBox.TabIndex = 1;
            this.photoBox.TabStop = false;
            this.photoBox.Click += new System.EventHandler(this.photoBox_Click);
            // 
            // nameTxt
            // 
            this.nameTxt.BackColor = System.Drawing.Color.Transparent;
            this.nameTxt.Font = new System.Drawing.Font("DIN Next LT Arabic", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.nameTxt.ForeColor = System.Drawing.SystemColors.Desktop;
            this.nameTxt.Location = new System.Drawing.Point(387, 580);
            this.nameTxt.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.nameTxt.Name = "nameTxt";
            this.nameTxt.Size = new System.Drawing.Size(203, 30);
            this.nameTxt.TabIndex = 2;
            this.nameTxt.Text = "DEFAULT VALUE";
            // 
            // weaponTxt
            // 
            this.weaponTxt.BackColor = System.Drawing.Color.Transparent;
            this.weaponTxt.Font = new System.Drawing.Font("DIN Next LT Arabic", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.weaponTxt.ForeColor = System.Drawing.SystemColors.Desktop;
            this.weaponTxt.Location = new System.Drawing.Point(387, 629);
            this.weaponTxt.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.weaponTxt.Name = "weaponTxt";
            this.weaponTxt.Size = new System.Drawing.Size(203, 30);
            this.weaponTxt.TabIndex = 3;
            this.weaponTxt.Text = "DEFAULT VALUE";
            // 
            // fireTxt
            // 
            this.fireTxt.BackColor = System.Drawing.Color.Transparent;
            this.fireTxt.Font = new System.Drawing.Font("DIN Next LT Arabic", 9.749999F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.fireTxt.ForeColor = System.Drawing.SystemColors.Desktop;
            this.fireTxt.Location = new System.Drawing.Point(387, 679);
            this.fireTxt.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.fireTxt.Name = "fireTxt";
            this.fireTxt.Size = new System.Drawing.Size(203, 30);
            this.fireTxt.TabIndex = 4;
            this.fireTxt.Text = "DEFAULT VALUE";
            // 
            // videoPlayer
            // 
            this.videoPlayer.Enabled = true;
            this.videoPlayer.Location = new System.Drawing.Point(30, 168);
            this.videoPlayer.Margin = new System.Windows.Forms.Padding(4);
            this.videoPlayer.Name = "videoPlayer";
            this.videoPlayer.OcxState = ((System.Windows.Forms.AxHost.State)(resources.GetObject("videoPlayer.OcxState")));
            this.videoPlayer.Size = new System.Drawing.Size(418, 272);
            this.videoPlayer.TabIndex = 0;
            this.videoPlayer.Enter += new System.EventHandler(this.axWindowsMediaPlayer1_Enter);
            // 
            // DisplayVideo
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.BackgroundImage = global::GUI_GP.Properties.Resources.interface_21;
            this.ClientSize = new System.Drawing.Size(1063, 724);
            this.Controls.Add(this.fireTxt);
            this.Controls.Add(this.weaponTxt);
            this.Controls.Add(this.nameTxt);
            this.Controls.Add(this.photoBox);
            this.Controls.Add(this.videoPlayer);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.MaximizeBox = false;
            this.MaximumSize = new System.Drawing.Size(1081, 771);
            this.MinimumSize = new System.Drawing.Size(1081, 771);
            this.Name = "DisplayVideo";
            this.Text = "SECURITY SYSTEM & FIRE DETECTION - DISPLAY VIDEO";
            this.FormClosing += new System.Windows.Forms.FormClosingEventHandler(this.DisplayVideo_FormClosing);
            this.Load += new System.EventHandler(this.DisplayVideo_Load);
            ((System.ComponentModel.ISupportInitialize)(this.photoBox)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.videoPlayer)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private AxWMPLib.AxWindowsMediaPlayer videoPlayer;
        private System.Windows.Forms.PictureBox photoBox;
        private System.Windows.Forms.Label nameTxt;
        private System.Windows.Forms.Label weaponTxt;
        private System.Windows.Forms.Label fireTxt;
    }
}