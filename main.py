"""
modularization with function
modularization with package
"""
import detector

if __name__ == '__main__':
    print('main app')
    result = detector.data_extraction()
    detector.show_data(result)
