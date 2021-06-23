VERSION:=`date '+%y%m%d'`
PYVERSION:=py37
tmp_dir:=_dist
ADDON:=bl_stru_utils

# Download OCC
ifeq ($(PLATFORM), win)
	OCE_URL:=https://anaconda.org/conda-forge/occt/7.5.1/download/win-64/occt-7.5.1-h60997fb_2.tar.bz2
	TBB_URL:=https://anaconda.org/conda-forge/tbb/2021.2.0/download/win-64/tbb-2021.2.0-h2d74725_0.tar.bz2

ifeq ($(PYVERSION), py37)
	PYTHONOCC_URL:=https://anaconda.org/conda-forge/pythonocc-core/7.5.1/download/win-64/pythonocc-core-7.5.1-py37h8c6f293_0.tar.bz2
	H5PY_URL:=https://anaconda.org/conda-forge/h5py/3.2.1/download/win-64/h5py-3.2.1-nompi_py37he280515_100.tar.bz2
endif
ifeq ($(PYVERSION), py39)
	PYTHONOCC_URL:=https://anaconda.org/conda-forge/pythonocc-core/7.5.1/download/win-64/pythonocc-core-7.5.1-py39h5d9d39a_0.tar.bz2
	H5PY_URL:=https://anaconda.org/conda-forge/h5py/3.2.1/download/win-64/h5py-3.2.1-nompi_py39hf27771d_100.tar.bz2
endif
endif

.PHONY: dist
dist:

ifndef PLATFORM
	$(error PLATFORM is not set)
endif

	# Establish work dirs
	rm -rf $(tmp_dir)
	mkdir -p $(tmp_dir)/working
	mkdir -p $(tmp_dir)/$(ADDON)
	cp -r $(ADDON)/* $(tmp_dir)/$(ADDON)/

	# Install OCC
	@echo "Starting download"
	cd $(tmp_dir)/working && wget $(PYTHONOCC_URL)
	cd $(tmp_dir)/working && tar -xjvf pythonocc-core*
	cd $(tmp_dir)/working && cp -r Lib/site-packages/OCC ../$(ADDON)/libs/site/packages/

	rm -rf $(tmp_dir)/working

	# Install OCE (Required by PythonOCC-core)
	mkdir $(tmp_dir)/working
	cd $(tmp_dir)/working && wget $(OCE_URL)
	cd $(tmp_dir)/working && tar -xjvf oc*
	cd $(tmp_dir)/working && cp -r Library/bin/* ../$(ADDON)/libs/site/packages/OCC/Core

	# Install TBB (Required by OCE)
	rm -rf $(tmp_dir)/working

	# Required by OpenCascade
	mkdir $(tmp_dir)/working
	cd $(tmp_dir)/working && wget $(TBB_URL)
	cd $(tmp_dir)/working && tar -xjvf tbb*
	cd $(tmp_dir)/working && cp -r bin/* ../$(ADDON)/libs/site/packages/OCC/Core/

	rm -rf $(tmp_dir)/working

	# Install H5PY
	mkdir $(tmp_dir)/working
	cd $(tmp_dir)/working && wget $(H5PY_URL)
	cd $(tmp_dir)/working && tar -xjvf h5*
	cd $(tmp_dir)/working && cp -r Lib/site-packages/* ../$(ADDON)/libs/site/packages/


.PHONY: clean
clean:
	rm -rf $(tmp_dir)