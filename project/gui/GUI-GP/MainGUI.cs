using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace GUI_GP
{
    public partial class MainGUI : Form
    {
        public MainGUI()
        {
            InitializeComponent();
        }       
        
        private void Form1_Load(object sender, EventArgs e)
        {
            using (var stream = File.Open("../../../../files/face.txt", FileMode.Truncate))
            {
                // Do nothing here, the file will be truncated
            }
            using (var stream = File.Open("../../../../files/detect_fire.txt", FileMode.Truncate))
            {
                // Do nothing here, the file will be truncated
            }
            using (var stream = File.Open("../../../../files/guns.txt", FileMode.Truncate))
            {
                // Do nothing here, the file will be truncated
            }
        }

        private void uploadBut_Click(object sender, EventArgs e)
        {
            OpenFileDialog fdlg = new OpenFileDialog();
            fdlg.Title = "UPLOAD YOUR VIDEO FILE";
            fdlg.Filter = "Video Files (*.mp4)|*.mp4";
            fdlg.FilterIndex = 1;
            fdlg.RestoreDirectory = true;
            if (fdlg.ShowDialog() == DialogResult.OK)
            {
                this.Hide();
                DisplayVideo videoForm =new DisplayVideo(fdlg.FileName.ToString(),this);
                using (StreamWriter writer = new StreamWriter("../../../../files/location of videos.txt"))
                {
                    writer.WriteLine("1");

                    writer.WriteLine(fdlg.FileName.ToString());
                    
                }

                videoForm.Show();
            }
        }

        private void realTimeBtn_Click(object sender, EventArgs e)
        {
            this.Hide();
            realTimeForm realForm = new realTimeForm(this);
            realForm.Show();
        }
    }
}
