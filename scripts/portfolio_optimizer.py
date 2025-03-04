import numpy as np
from scipy.optimize import minimize

def portfolio_performance(weights, annual_return, cov_matrix):
    portfolio_return = np.sum(annual_return * weights)
    portfolio_std_dev = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
    return portfolio_return, portfolio_std_dev

def negative_sharpe(weights, annual_return, cov_matrix):
    portfolio_return, portfolio_std_dev = portfolio_performance(weights, annual_return, cov_matrix)
    return -(portfolio_return / portfolio_std_dev)

def optimize_portfolio(annual_return, cov_matrix):
    constraints = ({'type': 'eq', 'fun': lambda x: np.sum(x) - 1})  # Weights sum to 1
    bounds = tuple((0, 1) for asset in range(len(annual_return)))
    initial_weights = np.array([1/len(annual_return)] * len(annual_return))

    # Pass additional arguments to the negative_sharpe function
    optimal = minimize(negative_sharpe, initial_weights, args=(annual_return, cov_matrix), 
                       method='SLSQP', bounds=bounds, constraints=constraints)
    
    return optimal.x