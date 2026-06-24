# ChaosSyncPy

A modular Python framework for chaotic synchronization, nonlinear control, disturbance analysis, and dynamical systems research.

## Overview

ChaosSyncPy is an open-source framework designed for the simulation and synchronization of nonlinear and chaotic dynamical systems. The project provides a flexible architecture for implementing master-slave synchronization schemes, control laws, disturbances, and numerical integration methods.

The framework is intended for researchers, students, and engineers working in areas such as:

* Chaotic systems
* Nonlinear control
* Synchronization
* Dynamical systems
* System identification

---

## Features

* Modular architecture
* Master-slave synchronization framework
* Configurable numerical solvers (`RK45`, `BDF`, `Radau`, etc.)
* Configurable disturbances
* Real-time and offline visualization
* Error convergence analysis
* Attractor visualization
* Easily extensible to new dynamical systems and controllers

---

## Installation

Clone the repository:

```bash
git clone https://github.com/felipeofugi/ChaosSyncPy.git
cd ChaosSyncPy
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

## Running a Simulation

Execute:

```bash
python main.py
```

Simulation parameters can be configured in:

```text
src/config.py
```

---

# Implemented Systems

## Lorenz System

The Lorenz system is one of the most studied chaotic systems and is defined by:

[
\dot{x} = \sigma(y-x)
]

[
\dot{y} = x(\rho-z)-y
]

[
\dot{z} = xy-\beta z
]

where:

* (\sigma = 10)
* (\rho = 28)
* (\beta = 8/3)

---

### Master-Slave Synchronization

The framework supports synchronization between a master and a slave Lorenz system through a configurable control law.

#### States

<p align="center">
  <img src="figures/fig_0_state_x.png" width="900">
</p>
<p align="center">
  <img src="figures/fig_1_state_y.png" width="900">
</p>
<p align="center">
  <img src="figures/fig_2_state_z.png" width="900">
</p>

---

#### Synchronization Error

<p align="center">
  <img src="figures/fig_4_errors.png" width="900">
</p>

---

#### Attractors

<p align="center">
  <img src="figures/attractor.png" width="900">
</p>

---

## Project Structure

```text
ChaosSyncPy/
│
├── data/
├── figures/
├── notebooks/
├── src/
│   ├── config.py
│   ├── controller.py
│   ├── disturbances.py
│   ├── plots.py
│   ├── synchronization.py
│   ├── system.py
│   └── __init__.py
│
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

---

## License

This project is distributed under the MIT License.

---

## Citation

If you use this project in academic research, please consider citing the repository in your publications.
