import os
from recipes.example import Example
from recipes.ner import Recipe_NER_BLSTM_CRF as NER

class MyModel(object):
    SAVE_NAME = 'ner'
    MODEL_DIR = 'model-data'

    """
    Model template. You can load your model parameters in __init__ from a location accessible at runtime
    """
    def __init__(self, bucket, model_key):
        """
        Add any initialization parameters. These will be passed at runtime from the graph definition parameters defined in your seldondeployment kubernetes resource manifest.
        """
        print("Initializing")
        print("bucket: " + bucket)
        print("model key: " + model_key)
        self.loaded = False
        self.recipe = None

        self.model_save_path = "./" + self.MODEL_DIR
        self.load()

    def load(self):
        print("start load model")
        save_name = os.path.join(self.model_save_path, self.SAVE_NAME)
        self.recipe = NER.restore_from_path(save_name)
        print("model loaded")
        self.loaded = True

    def predict(self, X, features_names=None):
        """
        Return a prediction.

        Parameters
        ----------
        X : array-like
        feature_names : array of feature names (optional)
        """
        examples = [Example(text) for text in X]
        exs = self.recipe.predict(examples)
        return exs

    def tags(self):
        return {"version": self.__version}

# aa = MyModel("", "")
# tt = ["【热点】沪深300三大期权上市，我国金融期权市场进入多标的运行新阶段记者丨吴善阳 张茜沪深300指数衍生出的三大期权品种昨天同日上市。分别是：在上交所上市交易的沪深300ETF期权合约，标的为华泰柏瑞沪深300ETF，在深交所上市交易的沪深300ETF期权合约，标的为嘉实沪深300ETF，在中金所上市交易的则是沪深300股指期权，这是我国资本市场首个指数期权产品。股指期权的上市，对我国资本市场健康稳定发展具有重要意义。股指期权成为管理资本市场风险的重要工具沪深300三大期权上市首日，认沽主力合约大幅上扬。其中，中金所沪深300股指期权沽2月4000合约收涨52.5%；上交所300ETF期权沽1月4000合约涨21.7%，深交所300ETF期权沽1月4000合约涨46.6%。证监会副主席方星海昨天在沪深300股指期权上市仪式上指出，股指期权是管理资本市场风险的重要工具，上市股指期权，有助于完善资本市场风险管理体系，吸引长期资金入市，对于推动资本市场深化改革，促进资本市场健康稳定发展具有重要意义。方星海：作为国际上发展成熟的风险管理工具，股指期权功能充分发挥后，能够反映标的指数波动率，帮助投资者灵活调整资产组合的风险收益结构，丰富交易策略，有助于引入不同风险偏好的投资者进入股票市场。市场表现符合预期，沪深300股指期权体现稳起步要求作为管理资本市场风险的重要工具，沪深300股指期权被视为金融市场的“保险”。新湖期货董事长马文胜说，开盘后的市场表现符合预期，价格与股指期货发现的价格接近，体现了稳起步的要求，说明产品设计、交易规则是科学、合理的。马文胜：因为是需要稳起步，所以说总体的交易量流动性还是非常不错的。那么从价格看，应该从它波动率、市场给出的波动率和理论波动率还是非常接近的。价格也非常贴近我们股指期货所发现的价格，所以说这个市场开始非常平稳，也达到了上市的目的，所以应该说合约设计的还是非常成功的。采取持仓限额，参与沪深300股指期权有门槛据了解，沪深300股指期权采取持仓限额，即同一客户某1月份的持仓限额为五千手。此外沪深300股指期权上市初期执行较为严格的交易限额制度。中国金融期货交易所期权事业部王琦说，根据金融期货交易者适当性制度，个人投资者参与沪深300股指期权，需要设有一定的门槛，就是我们通常所说的“三有一无”。王琦：根据金融期货交易者市场性制度，个人投资者参与沪深300股指期权需要设有一定的门槛，投资者必须要有资金，有交易，交易经历、有专业知识，并且无不量诚信记录，其中的资金门槛是50万元"]
# print(aa.predict(tt))