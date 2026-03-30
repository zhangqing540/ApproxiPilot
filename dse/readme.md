# DSE

## Overview

The `dse` component is the design space exploration module of the ApproxPilot framework. It is responsible for multi-objective optimization and automated exploration of approximate computing design configurations.

Given the predictions produced by the trained graph neural network models, this module explores the candidate design space and identifies Pareto-optimal solutions under multiple design objectives.

## Objectives

The exploration process considers the following objectives:

- Area
- Power
- Latency
- SSIM

## Role in ApproxPilot

Within the ApproxPilot framework, the `dse` component enables efficient search over approximate design candidates and supports Pareto-front construction for multi-objective optimization.
