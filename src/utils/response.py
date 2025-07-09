
from sdks.novavision.src.helper.package import PackageHelper
from components.CropExample.src.models.PackageModel import PackageModel, PackageConfigs, ConfigExecutor, CropExampleExecutorOutputs, CropExampleExecutorResponse, CropExampleExecutor, OutputImage


def build_response(context):
    outputImage = OutputImage(value=context.image)
    cropExampleExecutorOutputs= CropExampleExecutorOutputs(outputImage=outputImage)
    cropExampleExecutorResponse = CropExampleExecutorResponse(outputs=cropExampleExecutorOutputs)
    cropExampleExecutor=CropExampleExecutor(value=cropExampleExecutorResponse)
    configexecutor = ConfigExecutor(value=cropExampleExecutor)
    packageConfigs = PackageConfigs(executor=configexecutor)
    package = PackageHelper(packageModel=PackageModel, packageConfigs=packageConfigs)
    packageModel = package.build_model(context)
    return packageModel
