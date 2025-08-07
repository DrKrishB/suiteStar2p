# suiteStar2p

Brain registration, segmentation and analysis using a combination of suite2p, stardist, caiman, ANTs and my own algorithms

⚠️ **Important Notice**

This code is **not open source**.

You may **view** the code in this repository, but you may **not copy, reuse, or modify** any part of it without obtaining explicit permission from the author.

To request permission, please contact me via GitHub or [kbose@live.in](mailto:kbose@live.in).

---

## 💀 Tools Used

* [Suite2p](https://github.com/MouseLand/suite2p) — motion correction only
* [Stardist](https://github.com/stardist/stardist) — 2D segmentation extended to 4D
* [Caiman](https://github.com/flatironinstitute/CaImAn) — calcium trace denoising
* [ANTs](https://github.com/ANTsX/ANTs) — image registration
* Custom Python scripts for file handling and orchestration

---

## 🧪 Instructions

### 1. Convert raw 5D data to `.tif` files using ImageJ

#### 📂 Data Preparation

1. **Convert raw data to `.tif` files using ImageJ**

* Run the ImageJ macro:
  `raw1024x416dualchannel_bioformats.ijm`

* When prompted, navigate to the directory containing the folders with raw timelapse data.

* The macro will convert Thorlabs `.raw` files into dual-channel `.tif` format.

* You may delete the raw files after successful conversion.

#### 📀 Default values for raw data:

* Frame size: `1024 × 416`
* Pixel size: `0.977 µm`
* Z-step size: `12 µm`
* Planes: `17 z-planes + 2 flyback`

2. **Organize your data**

* Each timelapse should be in a separate folder
* Z-stacks should be in folders containing `"Zstack"` in their names

---

### ✨ Running the Motion Correction

3. **Prepare the motion correction script**

* Copy the file `suite2p_motionCorrection.py` into the directory containing the folders with timelapse data.

4. **Run the motion correction script**

From the same terminal (inside the directory with your data folders), run:

```bash
python -m suite2p_motionCorrection
```

👉 **Ensure you're in the same folder where the script and the timelapse folders are located.**

5. **Choose which data to process**

* The script will display all available folders, automatically skipping any that contain `"Zstack"` in the name.

* When prompted:

  * **Enter a number** to process a specific fish/timelapse folder, **OR**
  * Simply **press Enter** to process **all folders automatically**
