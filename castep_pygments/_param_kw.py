"""
CASTEP Parameters Keywords
"""
from pygments.lexer import words


PARAM = {
    "string": ("COMMENT", "VERBOSITY", "CONTINUATION", "REUSE",
               "CHECKPOINT", "TASK", "WRITE_CHECKPOINT", "CML_FILENAME",
               "LENGTH_UNIT", "MASS_UNIT", "TIME_UNIT", "CHARGE_UNIT", "SPIN_UNIT",
               "ENERGY_UNIT", "FORCE_UNIT", "VELOCITY_UNIT", "PRESSURE_UNIT",
               "INV_LENGTH_UNIT", "FREQUENCY_UNIT", "FORCE_CONSTANT_UNIT",
               "VOLUME_UNIT", "IR_INTENSITY_UNIT", "DIPOLE_UNIT", "EFIELD_UNIT",
               "BFIELD_UNIT", "ENTROPY_UNIT", "EFIELD_CHI2_UNIT",
               "DATA_DISTRIBUTION", "OPT_STRATEGY", "XC_FUNCTIONAL",
               "RELATIVISTIC_TREATMENT", "SEDC_SCHEME", "K_SCRN_DEN_FUNCTION",
               "NLXC_K_SCRN_DEN_FUNCTION", "K_SCRN_AVERAGING_SCHEME",
               "NLXC_K_SCRN_AVERAGING_SCHEME", "PSPOT_NONLOCAL_TYPE",
               "PSPOT_BETA_PHI_TYPE", "BASIS_PRECISION", "FINITE_BASIS_CORR",
               "SPIN_TREATMENT", "ELECTRONIC_MINIMIZER", "ELEC_METHOD",
               "METALS_METHOD", "SMEARING_SCHEME", "DIPOLE_CORRECTION", "DIPOLE_DIR",
               "ELEC_DUMP_FILE", "ELEC_RESTORE_FILE", "MIXING_SCHEME", "POPN_WRITE",
               "BS_XC_FUNCTIONAL", "GEOM_METHOD", "GEOM_PRECONDITIONER",
               "MD_ENSEMBLE", "MD_PATHINT_INIT", "MD_THERMOSTAT", "MD_BAROSTAT",
               "MD_EXTRAP", "MD_DAMPING_SCHEME", "MD_EQM_METHOD", "MD_HUG_METHOD",
               "MD_HUG_DIR", "OPTICS_XC_FUNCTIONAL", "TSSEARCH_METHOD",
               "TSSEARCH_LSTQST_PROTOCOL", "TSSEARCH_NEB_TANGENT_MODE",
               "TSSEARCH_NEB_METHOD", "PHONON_PRECONDITIONER",
               "PHONON_FINE_CUTOFF_METHOD", "PHONON_FINE_METHOD", "PHONON_METHOD",
               "PHONON_DFPT_METHOD", "SECONDD_METHOD", "PHONON_SUM_RULE_METHOD",
               "RAMAN_METHOD", "EFIELD_DFPT_METHOD", "EFIELD_IGNORE_MOLEC_MODES",
               "EFIELD_CALCULATE_NONLINEAR", "WANNIER_SPREAD_TYPE",
               "WANNIER_MIN_ALGOR", "WANNIER_RESTART", "MAGRES_TASK",
               "MAGRES_METHOD", "MAGRES_XC_FUNCTIONAL", "MAGRES_JCOUPLING_TASK",
               "ELNES_XC_FUNCTIONAL", "SPECTRAL_THEORY", "SPECTRAL_TASK",
               "SPECTRAL_XC_FUNCTIONAL", "TDDFT_XC_FUNCTIONAL", "TDDFT_METHOD",
               "TDDFT_EIGENVALUE_METHOD", "TDDFT_APPROXIMATION",
               "TDDFT_POSITION_METHOD", "BOUNDARY_TYPE", "DIELEC_EMB_CAVITY_TYPE",
               "DIELEC_EMB_FUNC_METHOD", "DIELEC_EMB_PARAM_SET", "MODOS_CHECKPOINT",
               "DELTASCF_CHECKPOINT", "DELTASCF_METHOD", "DELTASCF_DFTU_CHECKPOINT",
               "SOCKET_HOST"),

    "int": ("IPRINT", "RUN_TIME", "BACKUP_INTERVAL", "NUM_BACKUP_ITER",
            "PAGE_WVFNS", "RAND_SEED", "OPT_STRATEGY_BIAS", "NUM_FARMS",
            "NUM_PROC_IN_SMP", "NUM_PROC_IN_SMP_FINE", "MESSAGE_SIZE",
            "PAGE_EX_POT", "NLXC_PAGE_EX_POT", "PPD_SIZE_X", "NLXC_PPD_SIZE_X",
            "PPD_SIZE_Y", "NLXC_PPD_SIZE_Y", "PPD_SIZE_Z", "NLXC_PPD_SIZE_Z",
            "NLXC_DIV_CORR_NPTS_STEP", "FFT_MAX_PRIME_FACTOR",
            "FINITE_BASIS_NPOINTS", "NSPINS", "NEXTRA_BANDS", "NBANDS",
            "MAX_SD_STEPS", "MAX_CG_STEPS", "MAX_DIIS_STEPS",
            "ELEC_CONVERGENCE_WIN", "MAX_SCF_CYCLES", "SPIN_FIX",
            "NUM_OCC_CYCLES", "NUM_DUMP_CYCLES", "MIX_HISTORY_LENGTH",
            "BS_MAX_ITER", "BS_MAX_CG_STEPS", "BS_NEXTRA_BANDS", "BS_NBANDS",
            "GEOM_MAX_ITER", "GEOM_CONVERGENCE_WIN", "GEOM_SPIN_FIX",
            "GEOM_LBFGS_MAX_UPDATES", "GEOM_TPSD_ITERCHANGE", "MD_NUM_ITER",
            "MD_NUM_BEADS", "MD_PATHINT_NUM_STAGES", "MD_NHC_LENGTH",
            "MD_XLBOMD_HISTORY", "MD_DAMPING_RESET", "MD_ELEC_CONVERGENCE_WIN",
            "MD_SAMPLE_ITER", "OPTICS_NEXTRA_BANDS", "OPTICS_NBANDS",
            "TSSEARCH_QST_MAX_ITER", "TSSEARCH_LST_MAX_ITER",
            "TSSEARCH_CG_MAX_ITER", "TSSEARCH_MAX_PATH_POINTS",
            "TSSEARCH_NEB_MAX_ITER", "PHONON_MAX_CG_STEPS", "PHONON_MAX_CYCLES",
            "PHONON_CONVERGENCE_WIN", "EFIELD_MAX_CG_STEPS", "EFIELD_MAX_CYCLES",
            "EFIELD_CONVERGENCE_WIN", "THERMO_T_NPOINTS", "WANNIER_MAX_SD_STEPS",
            "WANNIER_PRINT_CUBE", "MAGRES_MAX_CG_STEPS", "MAGRES_CONVERGENCE_WIN",
            "MAGRES_MAX_SC_CYCLES", "DFPT_CONVERGENCE_WIN", "ELNES_NEXTRA_BANDS",
            "ELNES_NBANDS", "SPECTRAL_MAX_ITER", "SPECTRAL_MAX_STEPS_PER_ITER",
            "SPECTRAL_NEXTRA_BANDS", "SPECTRAL_NBANDS", "TDDFT_NUM_STATES",
            "TDDFT_SELECTED_STATE", "TDDFT_CONVERGENCE_WIN", "TDDFT_MAX_ITER",
            "TDDFT_NEXTRA_STATES", "GA_POP_SIZE", "GA_MAX_GENS", "MG_FD_ORDER",
            "MG_PADDING", "DELTASCF_MODE", "SOCKET_PORT"),

    "boolean": ("CALCULATE_STRESS", "CALCULATE_DENSDIFF", "CALCULATE_ELF",
                "CALCULATE_HIRSHFELD", "CALCULATE_POLARISATION",
                "CALCULATE_POLARIZATION", "CALCULATE_BERRY_PHASE", "PRINT_CLOCK",
                "PRINT_MEMORY_USAGE", "WRITE_NONE", "WRITE_FORMATTED_POTENTIAL",
                "WRITE_FORMATTED_DENSITY", "WRITE_FORMATTED_ELF", "WRITE_ORBITALS",
                "WRITE_CIF_STRUCTURE", "WRITE_CELL_STRUCTURE", "WRITE_BIB",
                "WRITE_OTFG", "WRITE_CST_ESP", "WRITE_BANDS", "WRITE_GEOM",
                "WRITE_MD", "CALC_MOLECULAR_DIPOLE", "CML_OUTPUT", "SEDC_APPLY",
                "SEDC_C9_XDM", "PPD_INTEGRAL", "NLXC_PPD_INTEGRAL", "IMPOSE_TRS",
                "NLXC_IMPOSE_TRS", "EXCHANGE_REFLECT_KPTS",
                "NLXC_EXCHANGE_REFLECT_KPTS", "RE_EST_K_SCRN", "NLXC_RE_EST_K_SCRN",
                "CALC_FULL_EX_POT", "NLXC_CALC_FULL_EX_POT", "NLXC_DIV_CORR_ON",
                "SPIN_ORBIT_COUPLING", "FIXED_NPW", "SPIN_POLARIZED",
                "SPIN_POLARISED", "FIX_OCCUPANCY", "POPN_CALCULATE",
                "PDOS_CALCULATE_WEIGHTS", "BS_RE_EST_K_SCRN", "BS_WRITE_EIGENVALUES",
                "GEOM_USE_LINMIN", "GEOM_PRECON_SCALE_CELL", "MD_USE_PATHINT",
                "MD_PATHINT_STAGING", "MD_EXTRAP_FIT", "MD_XLBOMD",
                "MD_OPT_DAMPED_DELTA_T", "MD_CELL_DAMP_RINGING", "MD_USE_PLUMED",
                "TSSEARCH_NEB_CLIMBING", "TSSEARCH_NEB_NORMED", "PHONON_CONST_BASIS",
                "PHONON_USE_KPOINT_SYMMETRY", "PHONON_CALCULATE_DOS",
                "PHONON_CALC_LO_TO_SPLITTING", "PHONON_SUM_RULE",
                "CALCULATE_BORN_CHARGES", "BORN_CHARGE_SUM_RULE", "CALCULATE_RAMAN",
                "PHONON_WRITE_FORCE_CONSTANTS", "PHONON_WRITE_DYNAMICAL",
                "EFIELD_CALC_ION_PERMITTIVITY", "THERMO_CALCULATE_HELMHOLTZ",
                "WANNIER_ION_MOMENTS", "WANNIER_ION_CUT", "WANNIER_ION_CMOMENTS",
                "MAGRES_WRITE_RESPONSE", "SPECTRAL_RE_EST_K_SCRN",
                "SPECTRAL_WRITE_EIGENVALUES", "SPECTRAL_RESTART", "GA_FIXED_N",
                "GA_BULK_SLICE", "USE_SMEARED_IONS", "WRITE_FORMATTED_DIELEC_PERM",
                "IMPLICIT_SOLVENT_APOLAR_TERM", "IMPLICIT_SOLVENT_RESCALE_APOLAR",
                "CALCULATE_MODOS", "CALCULATE_DELTASCF", "DELTASCF_EXCITE"),

    "defined": ("STOP"),

    "block": ("XC_DEFINITION", "BS_XC_DEFINITION",
              "OPTICS_XC_DEFINITION", "MAGRES_XC_DEFINITION", "ELNES_XC_DEFINITION",
              "SPECTRAL_XC_DEFINITION", "TDDFT_XC_DEFINITION", "MODOS_STATES",
              "DELTASCF_CONSTRAINTS", "DEVEL_CODE"),

    "real": ("XC_VXC_DERIV_EPSILON", "SEDC_SR_TS", "SEDC_D_TS",
             "SEDC_A1_XDM", "SEDC_SC_XDM", "SEDC_S6_G06", "SEDC_D_G06",
             "SEDC_LAMBDA_OBS", "SEDC_N_OBS", "SEDC_SR_JCHS", "SEDC_S6_JCHS",
             "SEDC_D_JCHS", "NLXC_EXCHANGE_FRACTION", "NLXC_DIV_CORR_TOL",
             "GRID_SCALE", "FINE_GRID_SCALE", "NELECTRONS", "CHARGE", "SPIN",
             "NUP", "NDOWN", "PERC_EXTRA_BANDS", "MIX_CHARGE_AMP", "MIX_SPIN_AMP",
             "MIX_KED_CHARGE_AMP", "MIX_KED_SPIN_AMP", "BS_PERC_EXTRA_BANDS",
             "GEOM_LINMIN_TOL", "GEOM_TPSD_INIT_STEPSIZE",
             "GEOM_PRECON_EXP_C_STAB", "GEOM_PRECON_EXP_A", "MD_HUG_COMPRESSION",
             "OPTICS_PERC_EXTRA_BANDS", "PHONON_FORCE_CONSTANT_CUT_SCALE",
             "PHONON_FORCE_CONSTANT_ELLIPSOID", "EFIELD_OSCILLATOR_Q",
             "WANNIER_SPREAD_TOL", "WANNIER_SD_STEP", "WANNIER_ION_CUT_FRACTION",
             "WANNIER_ION_CUT_TOL", "ELNES_PERC_EXTRA_BANDS",
             "SPECTRAL_PERC_EXTRA_BANDS", "GA_MUTATE_RATE", "GA_SPIN_MUTATE_RATE",
             "DIELEC_EMB_BULK_PERMITTIVITY", "IMPLICIT_SOLVENT_APOLAR_FACTOR",
             "DELTASCF_OVERLAP_CUTOFF", "DELTASCF_NET_SPIN_1",
             "DELTASCF_NET_SPIN_2"),

    "physical": ("SEDC_A2_XDM", "NLXC_EXCHANGE_SCREENING",
                 "NLXC_DIV_CORR_S_WIDTH", "CUT_OFF_ENERGY", "FINE_GMAX",
                 "FINE_CUT_OFF_ENERGY", "BASIS_DE_DLOGE", "FINITE_BASIS_SPACING",
                 "ELEC_TEMP", "ELEC_ENERGY_TOL", "ELEC_EIGENVALUE_TOL",
                 "ELEC_FORCE_TOL", "SMEARING_WIDTH", "EFERMI_TOL", "MIX_CHARGE_GMAX",
                 "MIX_SPIN_GMAX", "MIX_CUT_OFF_ENERGY", "MIX_METRIC_Q",
                 "MIX_KED_CHARGE_GMAX", "MIX_KED_SPIN_GMAX", "POPN_BOND_CUTOFF",
                 "BS_EIGENVALUE_TOL", "GEOM_ENERGY_TOL", "GEOM_FORCE_TOL",
                 "GEOM_DISP_TOL", "GEOM_STRESS_TOL", "GEOM_MODULUS_EST",
                 "GEOM_FREQUENCY_EST", "GEOM_PRECON_EXP_R_NN", "GEOM_PRECON_EXP_R_CUT",
                 "GEOM_PRECON_EXP_MU", "GEOM_PRECON_FF_C_STAB", "GEOM_PRECON_FF_R_CUT",
                 "MD_DELTA_T", "MD_TEMPERATURE", "MD_ION_T", "MD_CELL_T", "MD_NOSE_T",
                 "MD_LANGEVIN_T", "MD_ELEC_ENERGY_TOL", "MD_ELEC_EIGENVALUE_TOL",
                 "MD_ELEC_FORCE_TOL", "MD_EQM_ION_T", "MD_EQM_CELL_T", "MD_EQM_T",
                 "MD_HUG_T", "TSSEARCH_FORCE_TOL", "TSSEARCH_DISP_TOL",
                 "TSSEARCH_ENERGY_TOL", "TSSEARCH_NEB_SPRING_CONSTANT",
                 "PHONON_ENERGY_TOL", "PHONON_DOS_SPACING", "PHONON_DOS_LIMIT",
                 "PHONON_FINITE_DISP", "PHONON_FORCE_CONSTANT_CUTOFF",
                 "RAMAN_RANGE_LOW", "RAMAN_RANGE_HIGH", "EFIELD_ENERGY_TOL",
                 "EFIELD_FREQ_SPACING", "THERMO_T_START", "THERMO_T_STOP",
                 "THERMO_T_SPACING", "WANNIER_ION_RMAX", "MAGRES_CONV_TOL",
                 "DFPT_EIGENVALUE_TOL", "ELNES_EIGENVALUE_TOL",
                 "SPECTRAL_EIGENVALUE_TOL", "TDDFT_EIGENVALUE_TOL", "GA_MUTATE_AMP",
                 "GA_SPIN_MUTATE_AMP", "EXCITED_STATE_SCISSORS",
                 "IMPLICIT_SOLVENT_SURFACE_TENSION", "DELTASCF_SMEARING")
}
# Map words to REs
PARAM = {key: words(val, prefix=r"\b", suffix=r"\b").get() for key, val in PARAM.items()}