using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using WMPLib;
using AxWMPLib;

namespace GUI_GP
{
    public partial class DisplayVideo : Form
    {
        private Timer positionTimer; // Timer to update the position
        private double interval = 1.0;

        Form GUI;
        public DisplayVideo(string videoPath,Form mainGUI)
        {
            InitializeComponent();
            videoPlayer.URL = videoPath;
            videoPlayer.settings.autoStart = true;
            photoBox.Image = Properties.Resources._179_1796406_thinking_man_download_transparent_png_image_man_thinking;
            GUI=mainGUI;
        }
        private void readOutputs()
        {
            string facePath = "../../../../files/face.txt";

            string[] faceFromFile = File.ReadAllLines(facePath);

            string weaponPath = "../../../../files/guns.txt";
            string[] weaponFromFile = File.ReadAllLines(weaponPath);

            string firePath = "../../../../files/detect_fire.txt";
            string[] fireFromFile = File.ReadAllLines(firePath);
            if(faceFromFile.Length != 0)
            {
                string x = "../../../";
                string[] person = faceFromFile[0].Split(',');
                photoBox.Image = Image.FromFile(x+person[0]);
                nameTxt.Text = person[1];
            }
            if (weaponFromFile.Length != 0)
            {
                weaponTxt.Text = weaponFromFile[0];
            }
            if (fireFromFile.Length != 0)
            {
                fireTxt.Text = fireFromFile[0];
            }
     
        }
        private void axWindowsMediaPlayer1_Enter(object sender, EventArgs e)
        {

        }

        private void DisplayVideo_Load(object sender, EventArgs e)
        {
            StartPositionTimer();
        }

       
        private void StartPositionTimer()
        {
            positionTimer = new Timer();
            positionTimer.Interval = (int)(interval * 1000); // Convert interval to milliseconds
            positionTimer.Tick += PositionTimer_Tick;
            positionTimer.Start();
        }

        private void StopPositionTimer()
        {
            if (positionTimer != null)
            {
                positionTimer.Stop();
                positionTimer.Tick -= PositionTimer_Tick;
                positionTimer.Dispose();
                positionTimer = null;
            }
        }
        private void PositionTimer_Tick(object sender, EventArgs e)
        {
            // Check if the video is paused
            if (videoPlayer.playState == WMPPlayState.wmppsPlaying)
            {
                double currentPosition = videoPlayer.Ctlcontrols.currentPosition;
                double duration = videoPlayer.currentMedia.duration;

                  readOutputs();
                // Check if the end of the video is reached
                if (currentPosition >= duration)
                {
                    StopPositionTimer();
                }
            }
        }

        private void DisplayVideo_FormClosing(object sender, FormClosingEventArgs e)
        {
            GUI.Close();
        }

        private void photoBox_Click(object sender, EventArgs e)
        {

        }
    }
}
